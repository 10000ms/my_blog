# -*- coding: utf-8 -*-
from rest_framework import serializers

from django.contrib.auth.models import Group


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')
