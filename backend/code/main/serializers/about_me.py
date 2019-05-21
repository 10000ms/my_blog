# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.website_manage import WebsiteManage


class AboutMeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = WebsiteManage
        fields = (
            'url',
            'id',
            'about_me',
        )
