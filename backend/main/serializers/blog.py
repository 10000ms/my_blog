# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.blog import Blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'url',
            'id',
            'title',
            'author',
            'create_time',
            'last_change_time',
            'category',
            'tabs',
            'brief',
            'content',
            'read_count',
            'like_count',
        )
        read_only_fields = ('read_count', 'like_count')

    @staticmethod
    def validate_title(value):
        if 5 <= len(value) <= 30:
            return value
        raise serializers.ValidationError('标题必须为5-30个字符')

    @staticmethod
    def validate_author(value):
        if 1 <= len(value) <= 10:
            return value
        raise serializers.ValidationError('作者必须为5-30个字符')

    @staticmethod
    def validate_brief(value):
        if 1 <= len(value) <= 200:
            return value
        raise serializers.ValidationError('简介必须为1-200个字符')
