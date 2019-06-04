# -*- coding: utf-8 -*-
from uuid import uuid4

from ._base import BaseModelTest
from ..models.tab import Tab
from ..models.category import Category
from ..models.blog import Blog


class TestBlog(BaseModelTest):

    item_url = '/api/blog/'

    blog_key = [
        'id',
        'title',
        'creator',
        'author',
        'create_time',
        'last_change_time',
        'category',
        'tabs',
        'brief',
        'content',
        'read_count',
        'like_count',
        'is_recommend',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tab = None
        self.category = None

    def setUp(self):
        super().setUp()
        # 添加一些初始辅助数据
        self.tab = Tab.objects.create(title='测试标签{}'.format(uuid4().hex[:6]))
        self.category = Category.objects.create(title='测试类型{}'.format(uuid4().hex[:6]))
        b = Blog.objects.create(
            title=uuid4().hex[:6],
            creator=self.superuser,
            author=self.superuser.username,
            category=self.category,
            brief=uuid4().hex,
            content=uuid4().hex,
        )
        b.tabs.add(self.tab)

    def _base_get_blog_check(self, client):
        """
        基础的获取blog检测
        """
        res = client.get(self._restful_url())
        self.base_response_check(res)
        data = res.json()['data']
        self.assertIsInstance(data, list)
        # 只测试其中一个即可
        self.check_key_in_dict(self.blog_key, data[0])

    def test_user_get_blog(self):
        self._base_get_blog_check(self.user_client)

    def test_superuser_get_blog(self):
        self._base_get_blog_check(self.superuser_client)

    def test_not_login_user_get_blog(self):
        self._base_get_blog_check(self.not_login_user_client)
