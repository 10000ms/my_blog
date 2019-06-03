# -*- coding: utf-8 -*-
from uuid import uuid4

from ._base import BaseModelTest
from ..models.user import User


class TestUser(BaseModelTest):

    item_url = '/api/user/'

    def _base_get_user_check(self, client):
        """
        基础的获取category检测
        """
        res = client.get(self._restful_url())
        self.base_response_check(res)
        data = res.json()['data']
        self.assertIsInstance(data, list)
        return data

    def test_user_get_user(self):
        d = self._base_get_user_check(self.user_client)
        self.assertEqual(len(d), 1)
        self.assertEqual(d[0]['id'], self.user.id)

    def test_superuser_get_user(self):
        d = self._base_get_user_check(self.superuser_client)
        self.assertGreaterEqual(len(d), 2)

    def test_not_login_user_get_category(self):
        d = self._base_get_user_check(self.user_client)
        self.assertEqual(len(d), 0)

    def test_create_user(self):
        # 即使是超级用户也不能调用create接口
        res = self.superuser_client.post(self._restful_url(), {}, self.json_content_type)
        self.check_not_auth(res)

    def test_user_change_user(self):
        """
        普通用户默认只可以修改自己的头像，其他不可以修改
        所以这里有三个测试：
        1. 一个是修改其他用户的头像
        2. 一个是修改自己的头像
        3. 一个是修改自己的其他字段
        :return:
        """
        pass

    def test_not_login_user_change_user(self):
        pass

    def test_superuser_change_user(self):
        """
        超级用户应该能修改自己所有的信息
        :return:
        """
        pass
