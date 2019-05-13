# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from ...serializers.comment import CommentSerializer
from ...models.comment import Comment
from ...models.date_record import DateRecord
from ...permissions import IsCreatorOrReadOnly


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsCreatorOrReadOnly, )

    def create(self, request, *args, **kwargs):
        # 合计评论计数
        DateRecord.objects.add_comment_count()
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """
        自动创建创建者
        """
        serializer.save(creator=self.request.user)

    @action(detail=False, methods=['get'])
    def blog(self, request):
        blog_id = int(request.query_params.get('id'))
        comment = Comment.objects.comment_from_blog(blog_id)
        page_class = self.paginator
        comment_page = page_class.paginate_queryset(comment, request)
        comment_serializer = CommentSerializer(comment_page, many=True, context={'request': request})
        return page_class.get_paginated_response(comment_serializer.data)
