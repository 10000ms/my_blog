# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from rest_framework.response import Response

from utils.api_common import create_response
from ..models.blog import Blog
from ..serializers.blog import BlogSerializer


class MainIndex(APIView):

    @method_decorator(cache_page(60 * 10))
    def get(self, request):
        c = {
            'request': request,
        }
        blog = Blog.objects.index_info()
        serializer = BlogSerializer(blog, many=True, context=c)
        return Response(create_response(data=[serializer.data, serializer.data]))
