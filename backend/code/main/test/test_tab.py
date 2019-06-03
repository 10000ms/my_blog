# -*- coding: utf-8 -*-
from uuid import uuid4

from ._base import BaseModelTest
from ..models.tab import Tab


class TestTab(BaseModelTest):

    item_url = '/api/tab/'

    tab_key = [
        'id',
        'title',
        'count',
    ]

    def setUp(self):
        super().setUp()
        # 添加一个原始数据，保证数据库内的Tab不是空的
        Tab.objects.create(title=self._random_title())

    @staticmethod
    def _random_title():
        return '测试标签{}'.format(uuid4().hex[:6])

    def create_tab_test_data(self):
        return {
            'title': self._random_title(),
        }

    def _need_create_change_check(self, need, response, title):
        """
        因为create和change的need检查逻辑部分是一样的，所以放在这个方法里面
        :param need: 是否需要增加或者修改
        :type need: bool
        :param response: 原始返回
        :param title: 检查的tab title
        """
        if need:
            self.base_response_check(response)
            c = Tab.objects.filter(title=title)
            self.assertTrue(c.exists())
        else:
            self.check_not_auth(response)
            c = Tab.objects.filter(title=title)
            self.assertFalse(c.exists())

    def _base_get_tab_check(self, client):
        """
        基础的获取tab检测
        """
        res = client.get(self._restful_url())
        self.base_response_check(res)
        data = res.json()['data']
        self.assertIsInstance(data, list)
        # 只测试其中一个即可
        self.check_key_in_dict(self.tab_key, data[0])

    def test_user_get_tab(self):
        self._base_get_tab_check(self.user_client)

    def test_superuser_get_tab(self):
        self._base_get_tab_check(self.superuser_client)

    def test_not_login_user_get_tab(self):
        self._base_get_tab_check(self.not_login_user_client)

    def _base_create_test(self, client, need_create=False):
        """
        基础的创建tab检测
        """
        t = self.create_tab_test_data()
        res = client.post(self._restful_url(), t, self.json_content_type)
        self._need_create_change_check(need_create, res, t['title'])

    def test_user_create_tab(self):
        self._base_create_test(self.user_client)

    def test_superuser_create_tab(self):
        self._base_create_test(self.superuser_client, True)

    def test_not_login_user_create_tab(self):
        self._base_create_test(self.not_login_user_client)

    def _base_change_test(self, client, need_change=False):
        """
        基础的修改tab检测
        """
        # 先创建一个新的tab
        title = self._random_title()
        temp_tab = Tab.objects.create(title=title)
        # 再生成一个用于修改的信息
        t = self.create_tab_test_data()
        res = client.put(self._restful_url(temp_tab.id), t, self.json_content_type)
        self._need_create_change_check(need_change, res, t['title'])

    def test_user_change_tab(self):
        self._base_change_test(self.user_client)

    def test_superuser_change_tab(self):
        self._base_change_test(self.superuser_client, True)

    def test_not_login_user_change_tab(self):
        self._base_change_test(self.not_login_user_client)

    def _base_delete_test(self, client, need_delete=False):
        """
        基础的删除tab检测
        """
        # 先创建一个新的tab
        title = self._random_title()
        temp_tab = Tab.objects.create(title=title)
        res = client.delete(self._restful_url(temp_tab.id))
        if need_delete:
            self.check_success_response(res)
            c = Tab.objects.filter(title=title)
            self.assertFalse(c.exists())
        else:
            self.check_not_auth(res)
            c = Tab.objects.filter(title=title)
            self.assertTrue(c.exists())

    def test_user_delete_tab(self):
        self._base_delete_test(self.user_client)

    def test_superuser_delete_tab(self):
        self._base_delete_test(self.superuser_client, True)

    def test_not_login_user_delete_tab(self):
        self._base_delete_test(self.not_login_user_client)
