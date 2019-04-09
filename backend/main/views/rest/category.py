# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import (
    viewsets,
    permissions,
)

from ...serializers.category import CategorySerializer
from ...models.category import Category


class CategoryViewSet(viewsets.ModelViewSet):

    # category 不需要分页
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def list(self, request, *args, **kwargs):
        """
        增加查询排序
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # 更改返回时排序
        serializer.instance = sorted(queryset, key=lambda c: c.category_index())

        return Response(serializer.data)
