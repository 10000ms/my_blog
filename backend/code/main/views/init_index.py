# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.conf import settings
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from utils.api_common import create_response
from ..models.blog import Blog
from ..models.website_manage import WebsiteManage
from ..models.region_record import RegionRecord
from ..models.date_record import DateRecord
from ..serializers.blog import BlogSerializer
from ..serializers.website_manage import WebsiteManageSerializer
from ..serializers.user import UserSerializer


class InitIndex(APIView, PageNumberPagination):

    # blog和blog_recommend数据缓存时间（分钟）
    cache_minutes = 5

    def _blog_from_cache(self, context):
        """
        获取blog信息缓存，因为信息都一样，所以context为任意用户的即可
        """
        b = cache.get('cache_init_index_blog')
        if not b:
            blog = Blog.objects.all()
            blog_page = self.paginate_queryset(blog, self.request)
            blog_serializer = BlogSerializer(blog_page, many=True, context=context)
            # 同时保存分页信息
            d = {
                'blog': blog_serializer.data,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'count': self.page.paginator.count,
            }
            cache.set('cache_init_index_blog', d, 60 * settings.CACHE_TIME)
            b = d
        return b

    @staticmethod
    def _blog_recommend_from_cache(context):
        """
        获取blog_recommend信息缓存，因为信息都一样，所以context为任意用户的即可
        """
        b = cache.get('cache_init_index_blog_recommend')
        if not b:
            blog_recommend = Blog.objects.recommend()
            blog_recommend_serializer = BlogSerializer(blog_recommend, many=True, context=context)
            b = blog_recommend_serializer.data
            cache.set('cache_init_index_blog_recommend', b, 60 * settings.CACHE_TIME)
        return b

    @staticmethod
    def _website_manage_from_cache(context):
        """
        获取website_manage信息缓存，因为信息都一样，所以context为任意用户的即可
        """
        w = cache.get('cache_init_index_website_manage')
        if not w:
            website_manage = WebsiteManage.objects.all()[:1]
            website_manage_serializer = WebsiteManageSerializer(website_manage, many=True, context=context)
            w = website_manage_serializer.data
            if len(w) >= 1:
                # 存在记录则直接返回第一条，保证返回的是字典而不是列表
                w = website_manage_serializer.data[0]
            cache.set('cache_init_index_website_manage', w, 60 * settings.CACHE_TIME)
        return w

    @staticmethod
    def _count_data_from_cache(demo=False):
        """
        获取统计信息缓存
        :param demo: 是否是demo模式
        """
        if demo:
            c = cache.get('cache_init_index_count_demo_data')
            if not c:
                c = {
                    'day': DateRecord.objects.end_index_demo_data(),
                    'region': RegionRecord.objects.end_index_demo_data(),
                }
                cache.set('cache_init_index_count_demo_data', c, 60 * settings.CACHE_TIME)
        else:
            c = cache.get('cache_init_index_count_data')
            if not c:
                c = {
                    'day': DateRecord.objects.end_index_data(),
                    'region': RegionRecord.objects.end_index_data(),
                }
                cache.set('cache_init_index_count_data', c, 60 * settings.CACHE_TIME)
        return c

    def get(self, request):
        c = {
            'request': request,
        }
        # 根据前后台返回不同的数据
        mode = request.query_params.get('mode')
        if not mode:
            mode = 'front'
        # 用户部分，通用，不缓存
        user_serializer = UserSerializer(request.user, context=c)
        if mode == 'front':
            # 前台模式
            blog = self._blog_from_cache(c)
            d = {
                'blog': blog['blog'],
                'blog_recommend': self._blog_recommend_from_cache(c),
                'website_manage': self._website_manage_from_cache(c),
                'user': user_serializer.data,
                'page': {
                    'next': blog['next'],
                    'previous': blog['previous'],
                    'count': blog['count'],
                },
            }
        elif mode == 'end':
            # 后台模式
            # 确定用户权限
            if request.user.pk and request.user.is_staff:
                d = {
                    'website_manage': self._website_manage_from_cache(c),
                    'user': user_serializer.data,
                    'count_data': self._count_data_from_cache(),
                }
            elif request.user.pk and request.user.is_demo_user:
                # 展示用户模式
                d = {
                    'website_manage': self._website_manage_from_cache(c),
                    'user': user_serializer.data,
                    'count_data': self._count_data_from_cache(True),
                }
            else:
                raise Http404()
        else:
            d = None
        return Response(create_response(data=d))
