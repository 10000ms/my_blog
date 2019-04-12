# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from utils.api_common import create_response
from ..models.blog import Blog
from ..serializers.blog import BlogSerializer
from ..models.website_manage import WebsiteManage
from ..serializers.website_manage import WebsiteManageSerializer
from ..serializers.user import UserSerializer


class InitIndex(APIView, PageNumberPagination):

    @method_decorator(cache_page(60 * 10))
    def get(self, request):
        c = {
            'request': request,
        }
        blog = Blog.objects.all()
        blog_page = self.paginate_queryset(blog, self.request)
        blog_serializer = BlogSerializer(blog_page, many=True, context=c)
        blog_recommend = Blog.objects.recommend()
        blog_recommend_serializer = BlogSerializer(blog_recommend, many=True, context=c)
        website_manage = WebsiteManage.objects.all()[:1]
        website_manage_serializer = WebsiteManageSerializer(website_manage, many=True, context=c)
        user_serializer = UserSerializer(request.user, context=c)
        d = {
            'blog': blog_serializer.data,
            'blog_recommend': blog_recommend_serializer.data,
            'website_manage': website_manage_serializer.data,
            'user': user_serializer.data,
            'page': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'count': self.page.paginator.count,
            },
        }
        return Response(create_response(data=d))
