# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.tab import Tab


class TabSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tab
        fields = ('url', 'title')
