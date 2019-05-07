# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet
from django.contrib.auth import logout

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
        if User.objects.custom_login(request) is True:
            res = UserSerializer(request.user, context={'request': request}).data
            return Response(create_response(data=res))
        else:
            raise ValidationError('登陆失败')

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.user.is_authenticated:
            logout(request)
        return Response(create_response(msg='登出成功'))

    @action(detail=False, methods=['post'])
    def register(self, request):
        # 是否开放注册
        p = WebsiteManage.objects.all()[:1]
        if len(p) == 0 or not p.open_register:
            raise PermissionDenied('本网站不开放注册')
        if User.objects.custom_register(request) is True:
            res = UserSerializer(request.user, context={'request': request}).data
            return Response(create_response(data=res))
        else:
            raise ValidationError('注册失败')

    def create(self, request, *args, **kwargs):
        """
        取消原本的create方法
        """
        raise AuthenticationFailed()
