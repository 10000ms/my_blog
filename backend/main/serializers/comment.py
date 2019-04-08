# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.comment import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('url', 'id', 'title', 'creator', 'blog', 'content')
        depth = 1

    @staticmethod
    def validate_title(value):
        if 2 <= len(value) <= 15:
            return value
        raise serializers.ValidationError('标题必须为2-15个字符')

    @staticmethod
    def validate_content(value):
        if 2 <= len(value) <= 1000:
            return value
        raise serializers.ValidationError('评论内容长度为2-1000个字符')
