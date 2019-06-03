# -*- coding: utf-8 -*-
from ._base import BaseModelTest


class TestInitIndex(BaseModelTest):

    front_url = '/api/init-index/?mode=front'
    end_url = '/api/init-index/?mode=end'

    base_front_data_key = ['blog', 'blog_recommend', 'user', 'website_manage']
    base_end_data_key = ['count_data', 'user', 'website_manage']

    user_data_key = [
        'id',
        'username',
        'first_name',
        'last_name',
        'phone',
        'email',
        'profile',
        'is_author',
        'is_demo_user',
        'is_superuser',
    ]

    def _base_front_check(self, response, user=True):
        self.base_response_check(response)
        data = response.json()['data']
        self.check_key_in_dict(self.base_front_data_key, data)
        self.check_key_in_dict(self.website_manage_data_key, data['website_manage'])
        # 如果是用户模式，则检测用户相关的内容
        if user:
            self.check_key_in_dict(self.user_data_key, data['user'])
            user_id = data['user']['id']
            self.assertIsInstance(user_id, int)
            self.assertGreater(user_id, 0)

    def _base_front(self, client, super_user=False):
        res = client.get(self.front_url)
        self._base_front_check(res)
        user = res.json()['data']['user']
        self.check_key_in_dict(self.user_data_key, user)
        if super_user:
            self.assertEqual(user['id'], self.superuser.id)
            # 超级用户应该具有特殊权限
            self.assertTrue(user['is_author'])
            self.assertTrue(user['is_superuser'])
        else:
            self.assertEqual(user['id'], self.user.id)
            # 普通用户不应该具有特殊权限
            self.assertFalse(user['is_author'])
            self.assertFalse(user['is_superuser'])

    def test_user_front(self):
        """
        普通用户进入前台的行为检测
        """
        self._base_front(self.user_client)

    def test_superuser_front(self):
        """
        超级用户进入前台的行为检测
        """
        self._base_front(self.superuser_client, True)

    def test_not_login_user_front(self):
        """
        游客进入前台的行为检测
        """
        res = self.not_login_user_client.get(self.front_url)
        self._base_front_check(res, False)

    def test_user_end(self):
        """
        普通用户进入后台的行为检测
        """
        res = self.user_client.get(self.end_url)
        self.check_not_found(res)

    def test_superuser_end(self):
        """
        超级用户进入后台的行为检测
        """
        res = self.superuser_client.get(self.end_url)
        self.base_response_check(res)
        self.check_key_in_dict(self.base_end_data_key, res.json()['data'])

    def test_not_login_user_end(self):
        """
        游客用户进入后台的行为检测
        """
        res = self.not_login_user_client.get(self.end_url)
        self.check_not_found(res)
