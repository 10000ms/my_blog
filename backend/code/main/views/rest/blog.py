from django.core.cache import cache
from django.conf import settings
from django.db import transaction

# from ...tasks import main as celery_task
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)

from ...serializers.blog import (
    BlogSerializer,
    BlogManageSerializer,
)
from ...permissions import IsAuthorOrReadOnly
from ...models.blog import Blog
from utils.api_common import create_response
# from utils.es import ESControl


class BlogViewSet(ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    manage_serializer_class = BlogManageSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def perform_create(self, serializer):
        """
        自动创建创建者
        """
        serializer.save(creator=self.request.user)

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def retrieve(self, request, *args, **kwargs):
        """
        重写blog这个方法，增加阅读计数功能以及缓存支持
        """
        blog_id = int(kwargs[self.lookup_field])
        # with transaction.atomic():
        #     # 阅读计数
        #     celery_task.add_read_count.delay(blog_id)
        #     if settings.RECORD_REGION:
        #         # 增加来源地址的统计
        #         ip = self.get_client_ip(request)
        #         celery_task.add_ip.delay(ip)
        b = cache.get('blog_{}'.format(blog_id))
        if not b:
            o = self.get_object()
            serializer = self.get_serializer(o)
            b = serializer.data
            cache.set('blog_{}'.format(o.id), b, 60 * settings.CACHE_TIME)
        return Response(b)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        搜索
        """
        # search_content = request.query_params.get('query')
        # es = ESControl()
        # id_list = es.auto_id_search('blog', search_content, ['title', 'author', 'brief', 'content'])
        blog = Blog.objects.all()
        page_class = self.pagination_class()
        blog_page = page_class.paginate_queryset(blog, request)
        blog_serializer = BlogSerializer(blog_page, many=True, context={'request': request})
        return page_class.get_paginated_response(blog_serializer.data)

    def get_serializer_class(self):
        """
        管理员返回不同权限类
        """
        if self.request.user.is_staff:
            return self.manage_serializer_class
        return self.serializer_class

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def heart(self, request):
        # blog_id = int(request.data['id'])
        # # 合计的点赞计数
        # celery_task.add_like_count.delay(blog_id)
        return Response(create_response())

    @action(detail=False, methods=['post'], url_path='add-recommend', permission_classes=[IsAdminUser])
    def add_recommend(self, request):
        blog_id = int(request.data['id'])
        Blog.objects.add_recommend(blog_id)
        return Response(create_response())

    @action(detail=False, methods=['post'], url_path='cancel-recommend', permission_classes=[IsAdminUser])
    def cancel_recommend(self, request):
        blog_id = int(request.data['id'])
        Blog.objects.cancel_recommend(blog_id)
        return Response(create_response())
