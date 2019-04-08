# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ... import serializers
from ...models.comment import Comment


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = serializers.comment.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
