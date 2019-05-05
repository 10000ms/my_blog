# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from ...serializers.tab import TabSerializer
from ...serializers.blog import BlogSerializer
from ...models.tab import Tab
from ...models.blog import Blog
from .blog import BlogViewSet


class TabViewSet(ModelViewSet):

    # tabs 不需要分页
    pagination_class = None
    queryset = Tab.objects.all()
    serializer_class = TabSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    @action(detail=False, methods=['get'])
    def query(self, request):
        query_id = int(request.query_params.get('query'))
        blog = Blog.objects.filter(tabs__id__contains=query_id)
        page_class = BlogViewSet.pagination_class()
        blog_page = page_class.paginate_queryset(blog, request)
        blog_serializer = BlogSerializer(blog_page, many=True, context={'request': request})
        return page_class.get_paginated_response(blog_serializer.data)
