# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.comment import Comment
from ..models.user import User
from ..models.blog import Blog


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    creator_pk = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='creator', write_only=True
    )

    blog_pk = serializers.PrimaryKeyRelatedField(
        queryset=Blog.objects.all(), source='blog', write_only=True
    )

    class Meta:
        model = Comment
        fields = (
            'url',
            'id',
            'title',
            'creator',
            'creator_pk',
            'blog',
            'blog_pk',
            'content',
        )
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
