# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet
from django.contrib.auth.models import Group
from django.contrib.auth import (
    authenticate,
    login,
)
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError as BaseValidationError

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import (
    AuthenticationFailed,
    PermissionDenied,
    ValidationError,
)
from rest_framework.parsers import JSONParser

from utils.api_common import create_response
from ...serializers.user import UserSerializer
from ...models.user import User
from ...models.website_manage import WebsiteManage
from ...validator.auth import (
    validate_name,
    validate_username_password,
    validate_phone,
)


class UserViewSet(ModelViewSet):

    queryset = User.objects.none()
    queryset_manage = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    parser_classes = (JSONParser, )

    def get_queryset(self):
        """
        重写方法，针对不同权限用户提供不同的查询集
        """
        if self.request.user.is_staff:
            self.queryset = self.queryset_manage

        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    @action(detail=False, methods=['post'])
    def login(self, request):
        c = {
            'request': request,
        }
        if 'username' not in request.data or 'password' not in request.data:
            raise ValidationError('必须含有username, password')
        # 验证一下
        try:
            validate_username_password(request.data['username'])
            validate_username_password(request.data['password'])
        except BaseValidationError as e:
            raise ValidationError(e.messages)
        if not request.user.is_authenticated:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            if user:
                login(request, user)
            else:
                raise AuthenticationFailed('用户名或密码错误')
        d = UserSerializer(request.user, context=c)
        return Response(create_response(data=d.data))

    @action(detail=False, methods=['post'])
    def register(self, request):
        # 是否开放注册
        p = WebsiteManage.objects.all()[:1]
        if len(p) == 0 or not p.open_register:
            raise PermissionDenied('本网站不开放注册')
        c = {
            'request': request,
        }
        # TODO 抽离到model层做这个功能
        if list(filter(lambda a: a not in request.data, ['username', 'email', 'password', 'first_name', 'last_name',
                                                         'phone'])):
            raise ValidationError('必须含有username, email, password, first_name, last_name, phone')
        # 验证一下
        try:
            validate_username_password(request.data['username'])
            validate_username_password(request.data['password'])
            EmailValidator()(request.data['email'])
            validate_phone(request.data['phone'])
            validate_name(request.data['first_name'])
            validate_name(request.data['last_name'])
        except BaseValidationError as e:
            raise ValidationError(e.messages)
        # 重复性检测
        username_user = len(User.objects.filter(username=request.data['username']))
        email_user = len(User.objects.filter(email=request.data['email']))
        phone_user = len(User.objects.filter(phone=request.data['phone']))
        if username_user or email_user or phone_user:
            raise ValidationError('用户名或email或电话重复')
        user = User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            phone=request.data['phone'],
            password=request.data['password'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name']
        )
        user_group = Group.objects.filter(pk=1)
        user.groups.add(user_group.id)
        user.save()
        login(request, user)
        d = UserSerializer(request.user, context=c)
        return Response(create_response(data=d))

    def create(self, request, *args, **kwargs):
        """
        取消原本的create方法
        """
        raise AuthenticationFailed()
