# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ...serializers.website_manage import WebsiteManageSerializer
from ...permissions import ReadOnly
from ...models.website_manage import WebsiteManage


class WebsiteManageViewSet(viewsets.ModelViewSet):

    # website_manage 不需要分页
    pagination_class = None
    # 这个数据库只对第一条进行操作管理
    queryset = WebsiteManage.objects.all()[:1]
    serializer_class = WebsiteManageSerializer
    permission_classes = (permissions.IsAdminUser | ReadOnly, )
