# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.blog import Blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'url',
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
