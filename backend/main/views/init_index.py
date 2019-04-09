# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from rest_framework.response import Response

from utils.api_common import create_response
from ..models.blog import Blog
from ..serializers.blog import BlogSerializer
from ..models.website_manage import WebsiteManage
from ..serializers.website_manage import WebsiteManageSerializer


class MainIndex(APIView):

    @method_decorator(cache_page(60 * 10))
    def get(self, request):
        c = {
            'request': request,
        }
        blog = Blog.objects.index_info()
        blog_serializer = BlogSerializer(blog, many=True, context=c)
        blog_recommend = Blog.objects.recommend()
        blog_recommend_serializer = BlogSerializer(blog_recommend, many=True, context=c)
        website_manage = WebsiteManage.objects.all()[:1]
        website_manage_serializer = WebsiteManageSerializer(website_manage, many=True, context=c)
        d = {
            'blog': blog_serializer.data,
            'blog_recommend': blog_recommend_serializer.data,
            'website_manage': website_manage_serializer.data,
        }
        return Response(create_response(data=d))
