from django.db.models.deletion import ProtectedError

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAdminUser

from utils.api_common import create_response
from ...permissions import ReadOnly
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
    permission_classes = (IsAdminUser | ReadOnly, )

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

    def destroy(self, request, *args, **kwargs):
        """
        重写方法，触犯ProtectedError时正确返回
        """
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(create_response(msg='关联对象不能直接删除！'), status=400)
        return Response(status=HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def query(self, request):
        query_id = int(request.query_params.get('query'))
        blog = Blog.objects.query_category(query_id)
        page_class = BlogViewSet.pagination_class()
        blog_page = page_class.paginate_queryset(blog, request)
        blog_serializer = BlogSerializer(blog_page, many=True, context={'request': request})
        return page_class.get_paginated_response(blog_serializer.data)
