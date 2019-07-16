from django.contrib.auth import logout

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import (
    AuthenticationFailed,
    ValidationError,
)
from rest_framework.parsers import JSONParser

from utils.api_common import create_response
from ...permissions import UserCannotDelete
from ...serializers.user import UserSerializer
from ...models.user import User
from ...models.website_manage import WebsiteManage


class UserViewSet(ModelViewSet):

    queryset = User.objects.none()
    queryset_manage = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    parser_classes = (JSONParser, )
    permission_classes = (UserCannotDelete, )

    not_superuser_update_field = ['profile']

    def get_queryset(self):
        """
        重写方法，针对不同权限用户提供不同的查询集
        """
        if self.request.user.is_staff:
            self.queryset = self.queryset_manage
        elif self.request.user.id:
            self.queryset = User.objects.filter(id=self.request.user.id)
        return super().get_queryset()

    @action(detail=False, methods=['post'])
    def login(self, request):
        if User.objects.custom_login(request) is True:
            res = UserSerializer(request.user, context={'request': request}).data
            return Response(create_response(data=res))
        else:
            raise ValidationError('登陆失败')

    @action(detail=False, methods=['post'])
    def demo(self, request):
        # 是否开放demo模式
        p = WebsiteManage.objects.all()
        if p.count() == 0 or not p[0].demo_model:
            raise ValidationError('本网站不开放注册')
        else:
            if User.objects.demo_login(request) is True:
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
        p = WebsiteManage.objects.all()
        if p.count() == 0 or not p[0].open_register:
            raise ValidationError('本网站不开放注册')
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

    def update(self, request, *args, **kwargs):
        """
        重写方法限制普通用户的修改字段
        """
        if request.user.id and not request.user.is_staff:
            for f in request.data:
                if f not in self.not_superuser_update_field:
                    raise AuthenticationFailed('普通用户只能修改{}！'.format(','.join(self.not_superuser_update_field)))
        return super().update(request, *args, **kwargs)
