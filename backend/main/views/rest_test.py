# -*- coding: utf-8 -*-
from rest_framework import viewsets

from .. import serializers

from django.contrib.auth.models import Group
from ..models.blog import Blog
from ..models.category import Category
from ..models.tab import Tab
from ..models.website_manage import WebsiteManage
from ..models.user import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.user.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.group.GroupSerializer


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = serializers.blog.BlogSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = serializers.category.CategorySerializer


class TabViewSet(viewsets.ModelViewSet):

    queryset = Tab.objects.all()
    serializer_class = serializers.tab.TabSerializer


class WebsiteManageViewSet(viewsets.ModelViewSet):

    queryset = WebsiteManage.objects.all()
    serializer_class = serializers.website_manage.WebsiteManageSerializer
