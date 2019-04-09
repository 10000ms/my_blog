# -*- coding: utf-8 -*-
from rest_framework import viewsets

from ...serializers.blog import BlogSerializer
from ...permissions import IsAuthorOrReadOnly
from ...models.blog import Blog


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        """
        重写blog这个方法，增加阅读计数功能
        """
        o = self.get_object()
        o.read_count += 1
        o.save()
        return super().retrieve(request, *args, **kwargs)
