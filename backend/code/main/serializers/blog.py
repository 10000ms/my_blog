from rest_framework import serializers

from ..models.blog import Blog
from ..models.category import Category
from ..models.tab import Tab
from .tab import TabSerializer
from .category import CategorySerializer


class BaseMeta:

    model = Blog
    fields = (
        'url',
        'id',
        'title',
        'creator',
        'author',
        'create_time',
        'last_change_time',
        'category',
        'category_pk',
        'tabs',
        'tabs_pk',
        'brief',
        'content',
        'read_count',
        'like_count',
        'is_recommend',
    )
    read_only_fields = ('read_count', 'like_count', 'is_recommend')
    depth = 1


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.CharField(source='creator.username', read_only=True)

    category_pk = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    tabs_pk = serializers.PrimaryKeyRelatedField(
        queryset=Tab.objects.all(), source='tabs', write_only=True, many=True
    )

    tabs = TabSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    @staticmethod
    def validate_title(value):
        if 5 <= len(value) <= 30:
            return value
        raise serializers.ValidationError('标题必须为5-30个字符')

    @staticmethod
    def validate_author(value):
        if 1 <= len(value) <= 10:
            return value
        raise serializers.ValidationError('作者必须为1-10个字符')

    @staticmethod
    def validate_brief(value):
        if 1 <= len(value) <= 200:
            return value
        raise serializers.ValidationError('简介必须为1-200个字符')

    class Meta(BaseMeta):
        pass


class BlogManageSerializer(BlogSerializer):
    """
    管理员类，可以修改是否推荐
    """

    class Meta(BaseMeta):
        read_only_fields = ('read_count', 'like_count')
