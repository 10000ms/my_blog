# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ...serializers.blog import (
    BlogSerializer,
    BlogManageSerializer,
)
from ...permissions import IsAuthorOrReadOnly
from ...models.blog import Blog
from utils.api_common import create_response


class BlogViewSet(ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    manage_serializer_class = BlogManageSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        """
        重写blog这个方法，增加阅读计数功能
        """
        o = self.get_object()
        o.read_count += 1
        o.save()
        return super().retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        """
        管理员返回不同权限类
        """
        if self.request.user.is_staff:
            return self.manage_serializer_class
        return self.serializer_class

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def heart(self, request):
        blog_id = int(request.data['id'])
        Blog.objects.heart(blog_id)
        return Response(create_response())
