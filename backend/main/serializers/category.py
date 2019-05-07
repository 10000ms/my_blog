# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.category import Category


class BaseCategorySerializer(serializers.HyperlinkedModelSerializer):

    father_category_pk = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='father_category', write_only=True, allow_null=True
    )

    @staticmethod
    def validate_title(value):
        if 2 <= len(value) <= 15:
            return value
        raise serializers.ValidationError('类型必须为2-15个字符')

    def validate(self, data):
        # self.instance获取模型类实例
        # data['father_category'] 获取修改后的father_category模型类实例
        if 'father_category' in data and self.instance and data['father_category']:
            # 检测循环
            check_ids = [self.instance.id, ]
            f = data['father_category']
            while f:
                if f.id in check_ids:
                    raise serializers.ValidationError('类型循环！')
                else:
                    check_ids.append(f.id)
                    f = f.father_category
        return data

    class Meta:
        model = Category
        fields = (
            'url',
            'id',
            'title',
            'father_category',
            'father_category_pk',
            'count',
        )
        depth = 1


class CategorySerializer(BaseCategorySerializer):
    """
    使得一层的father_category可以那得到id
    """

    father_category = BaseCategorySerializer(read_only=True)
