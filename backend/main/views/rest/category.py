# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from ...serializers.category import CategorySerializer
from ...models.category import Category
from ...serializers.blog import BlogSerializer
from ...models.blog import Blog
from .blog import BlogViewSet


class CategoryViewSet(ModelViewSet):

    # category 不需要分页
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

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

    @action(detail=False, methods=['get'])
    def query(self, request):
        query_id = int(request.query_params.get('query'))
        blog = Blog.objects.query_category(query_id)
        page_class = BlogViewSet.pagination_class()
        blog_page = page_class.paginate_queryset(blog, request)
        blog_serializer = BlogSerializer(blog_page, many=True, context={'request': request})
        return page_class.get_paginated_response(blog_serializer.data)
