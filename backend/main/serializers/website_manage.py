# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.website_manage import WebsiteManage


class WebsiteManageSerializer(serializers.HyperlinkedModelSerializer):

    @staticmethod
    def validate_website_name(value):
        if 2 <= len(value) <= 15:
            return value
        raise serializers.ValidationError('网站名必须为2-15个字符')

    class Meta:
        model = WebsiteManage
        fields = (
            'url',
            'id',
            'about_me',
            'website_name',
            'ICP_number',
            'website_image',
            'ad_1',
            'ad_2',
            'github',
            'email',
            'Friendship_link',
        )
