# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ... import serializers
from ... import permissions as custom_permissions
from ...models.website_manage import WebsiteManage


class WebsiteManageViewSet(viewsets.ModelViewSet):

    # website_manage 不需要分页
    pagination_class = None
    # 这个数据库只对第一条进行操作管理
    queryset = WebsiteManage.objects.all()[:1]
    serializer_class = serializers.website_manage.WebsiteManageSerializer
    permission_classes = (permissions.IsAdminUser | custom_permissions.ReadOnly, )
