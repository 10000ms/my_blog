# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.category import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'id', 'title', 'father_category')
        extra_kwargs = {'father_category': {'required': False}}

    @staticmethod
    def validate_title(value):
        if 2 <= len(value) <= 15:
            return value
        raise serializers.ValidationError('类型必须为2-15个字符')

    def validate(self, data):
        # self.instance获取模型类实例
        # data['father_category'] 获取修改后的father_category模型类实例
        if data['father_category'] and data['father_category'].id == self.instance.id:
            raise serializers.ValidationError('父类型不能是自己！')
        return data
