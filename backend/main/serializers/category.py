# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.category import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'title', 'father_category')
