# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from ...serializers.website_manage import WebsiteManageSerializer
from ...permissions import ReadOnly
from ...models.website_manage import WebsiteManage


class WebsiteManageViewSet(ModelViewSet):

    # website_manage 不需要分页
    pagination_class = None
    # 这个数据库只对第一条进行操作管理
    queryset = WebsiteManage.objects.all()[:1]
    serializer_class = WebsiteManageSerializer
    permission_classes = (IsAdminUser | ReadOnly, )
