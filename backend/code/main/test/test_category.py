# -*- coding: utf-8 -*-
from uuid import uuid4

from ._base import BaseModelTest
from ..models.category import Category


class TestCategory(BaseModelTest):

    item_url = '/api/category/'

    tab_key = [
        'id',
        'title',
        'father_category',
        'count',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_category = None

    def setUp(self):
        super().setUp()
        # 添加一个原始数据，保证数据库内的Category不是空的,并且作为父类型
        self.base_category = self._add_category_to_db()

    @staticmethod
    def _random_title():
        return '测试类型{}'.format(uuid4().hex[:6])

    def create_category_test_data(self):
        return {
            'title': self._random_title(),
            # 创建使用的是father_category_pk代表father_category
            'father_category_pk': self.base_category.id,
        }

    def _need_create_change_check(self, need, response, title):
        """
        因为create和change的need检查逻辑部分是一样的，所以放在这个方法里面
        :param need: 是否需要增加或者修改
        :type need: bool
        :param response: 原始返回
        :param title: 检查的category title
        """
        c = Category.objects.filter(title=title)
        if need:
            self.base_response_check(response)
            self.assertTrue(c.exists())
        else:
            self.check_not_auth(response)
            self.assertFalse(c.exists())

    def _base_get_category_check(self, client):
        """
        基础的获取category检测
        """
        res = client.get(self._restful_url())
        self.base_response_check(res)
        data = res.json()['data']
        self.assertIsInstance(data, list)
        # 只测试其中一个即可
        self.check_key_in_dict(self.tab_key, data[0])

    def test_user_get_category(self):
        self._base_get_category_check(self.user_client)

    def test_superuser_get_category(self):
        self._base_get_category_check(self.superuser_client)

    def test_not_login_user_get_category(self):
        self._base_get_category_check(self.not_login_user_client)

    def _base_create_test(self, client, need_create=False):
        """
        基础的创建category检测
        """
        t = self.create_category_test_data()
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
        基础的修改category检测
        """
        # 先创建一个新的category
        title = self._random_title()
        temp_tab = Category.objects.create(title=title)
        # 再生成一个用于修改的信息
        t = self.create_category_test_data()
        res = client.put(self._restful_url(temp_tab.id), t, self.json_content_type)
        self._need_create_change_check(need_change, res, t['title'])

    def test_user_change_category(self):
        self._base_change_test(self.user_client)

    def test_superuser_change_category(self):
        self._base_change_test(self.superuser_client, True)

    def test_not_login_user_change_category(self):
        self._base_change_test(self.not_login_user_client)

    def _base_delete_test(self, client, need_delete=False):
        """
        基础的删除category检测
        """
        # 先创建一个新的tab
        title = self._random_title()
        temp_tab = Category.objects.create(title=title)
        res = client.delete(self._restful_url(temp_tab.id))
        c = Category.objects.filter(title=title)
        if need_delete:
            self.check_success_response(res)
            self.assertFalse(c.exists())
        else:
            self.check_not_auth(res)
            self.assertTrue(c.exists())

    def test_user_delete_category(self):
        self._base_delete_test(self.user_client)

    def test_superuser_delete_father_category(self):
        """
        测试超级用户删除father_category的情况
        """
        # 先取出father category的title防止如果删除后拿不到
        t = self.base_category.title
        # 往father category中加入一个child category
        Category.objects.create(title=self._random_title(), father_category=self.base_category)
        res = self.superuser_client.delete(self._restful_url(self.base_category.id))
        self.check_bad_request(res)
        c = Category.objects.filter(title=t)
        self.assertTrue(c.exists())

    def test_superuser_delete_child_category(self):
        """
        测试超级用户删除child_category的情况
        """
        self._base_delete_test(self.superuser_client, True)

    def test_not_login_user_delete_category(self):
        self._base_delete_test(self.not_login_user_client)
