# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from .. import serializers
from .. import permissions as custom_permissions

from ..models.blog import Blog
from ..models.category import Category
from ..models.tab import Tab
from ..models.website_manage import WebsiteManage
from ..models.user import User


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.user.UserSerializer
    permission_classes = (permissions.IsAdminUser | custom_permissions.OpenRegister, )


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = serializers.blog.BlogSerializer
    permission_classes = (custom_permissions.IsAuthorOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        """
        重写blog这个方法，增加阅读计数功能
        """
        o = self.get_object()
        o.read_count += 1
        o.save()
        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = serializers.category.CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class TabViewSet(viewsets.ModelViewSet):

    queryset = Tab.objects.all()
    serializer_class = serializers.tab.TabSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class WebsiteManageViewSet(viewsets.ModelViewSet):

    # 这个数据库只对第一条进行操作管理
    queryset = WebsiteManage.objects.all()[:1]
    serializer_class = serializers.website_manage.WebsiteManageSerializer
    permission_classes = (permissions.IsAdminUser | custom_permissions.ReadOnly, )
