# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from ...serializers.website_manage import WebsiteManageSerializer
from ...permissions import ReadOnly
from ...models.website_manage import WebsiteManage


class WebsiteManageViewSet(ModelViewSet):

    # website_manage 不需要分页
    pagination_class = None
    queryset = WebsiteManage.objects.all()
    serializer_class = WebsiteManageSerializer
    permission_classes = (IsAdminUser | ReadOnly, )

    def list(self, request, *args, **kwargs):
        """
        返回单个对象
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # 返回单个对象
        res = serializer.data
        if isinstance(res, list) and len(res) > 0:
            res = res[0]

        return Response(res)
