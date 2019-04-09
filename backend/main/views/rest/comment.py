# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ...serializers.comment import CommentSerializer
from ...models.comment import Comment


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
