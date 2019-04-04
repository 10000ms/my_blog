# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.tab import Tab


class TabSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tab
        fields = ('url', 'id', 'title')

    @staticmethod
    def validate_title(value):
        if 2 <= len(value) <= 15:
            return value
        raise serializers.ValidationError('标签必须为2-15个字符')
