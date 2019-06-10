# -*- coding: utf-8 -*-
from uuid import uuid4

from django.test import Client

from ._base import BaseModelTest
from ..models.user import User


class TestUser(BaseModelTest):

    item_url = '/api/user/'

    def _base_get_user_check(self, client):
        """
        基础的获取category检测
        """
        res = client.get(self._restful_url())
        self._base_response_check(res)
        data = res.json()['data']
        self.assertIsInstance(data, list)
        return data

    def _user_login_check(self, data, user=None):
        """
        通过获取的数据检查是否为登陆的user
        """
        self.assertEqual(len(data), 1)
        if user:
            self.assertEqual(data[0]['id'], user.id)

    def _not_login_check(self, data):
        """
        通过获取的数据检查是否为未登陆的
        """
        self.assertEqual(len(data), 0)

    def test_user_get_user(self):
        d = self._base_get_user_check(self.user_client)
        self._user_login_check(d, self.user)

    def test_superuser_get_user(self):
        d = self._base_get_user_check(self.superuser_client)
        self.assertGreaterEqual(len(d), 2)

    def test_not_login_user_get_user(self):
        d = self._base_get_user_check(self.not_login_user_client)
        self._not_login_check(d)

    def test_create_user(self):
        # 即使是超级用户也不能调用create接口
        res = self.superuser_client.post(self._restful_url(), {}, self.json_content_type)
        self._check_not_auth(res)

    @staticmethod
    def _create_email():
        return '{}@test.com'.format(uuid4().hex[:8])

    def test_user_change_user(self):
        """
        普通用户默认只可以修改自己的头像，其他不可以修改
        所以这里有三个部分的测试：
        1. 一个是修改其他用户的头像
        2. 一个是修改自己的头像
        3. 一个是修改自己的其他字段
        """
        profile = 'http://img.mp.itc.cn/upload/20160415/842805e6aa924d44ab620e8a27678239.jpg'
        # 修改自己头像
        res_1 = self.user_client.put(
            self._restful_url(self.user.id),
            {'profile': profile},
            self.json_content_type,
        )
        self._check_success_response(res_1)
        self.user.refresh_from_db()
        self.assertEqual(self.user.profile, profile)
        # 修改其他人头像
        res_2 = self.user_client.put(
            self._restful_url(self.superuser.id),
            {'profile': profile},
            self.json_content_type,
        )
        self._check_not_found(res_2)
        self.user.refresh_from_db()
        self.assertNotEqual(self.superuser.profile, profile)
        # 修改自己其他字段
        email = self._create_email()
        res_3 = self.user_client.put(
            self._restful_url(self.user.id),
            {'email': email},
            self.json_content_type,
        )
        self._check_not_auth(res_3)
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.email, email)

    def test_not_login_user_change_user(self):
        res = self.not_login_user_client.put(self._restful_url(self.user.id), {}, self.json_content_type)
        self._check_not_found(res)

    def test_user_delete_user(self):
        res = self.user_client.delete(self._restful_url(self.user.id))
        self._check_not_auth(res)

    def test_not_login_user_delete_user(self):
        res = self.not_login_user_client.delete(self._restful_url(self.user.id))
        self._check_not_auth(res)

    def test_login(self):
        c = Client()
        login_dict = {
            'username': self.user_username,
            'password': self.user_password,
        }
        res = c.post(self._restful_url('login'), login_dict, self.json_content_type)
        self._check_success_response(res)
        # 验证是否成功登录
        d = self._base_get_user_check(c)
        self._user_login_check(d, self.user)

    def test_logout(self):
        c = Client()
        c.login(username=self.user_username, password=self.user_password)
        res = c.post(self._restful_url('logout'), content_type=self.json_content_type)
        self._check_success_response(res)
        # 验证是否成功登出
        d = self._base_get_user_check(c)
        self._not_login_check(d)

    def test_demo(self):
        """
        demo涉及两种情况：
        一种是开放demo，要成功登录
        一种是没开放demo，不能登录
        """
        # 默认情况是关闭demo的
        # 先测试没开放demo的情况
        c = Client()
        res_1 = c.post(self._restful_url('demo'), {}, self.json_content_type)
        self._check_bad_request(res_1)
        d = self._base_get_user_check(c)
        self._not_login_check(d)
        try:
            # 开启demo再测试
            self.website_manage.demo_model = True
            self.website_manage.save()
            res_2 = c.post(self._restful_url('demo'), {}, self.json_content_type)
            self._base_response_check(res_2)
            d = self._base_get_user_check(c)
            self._user_login_check(d)
        finally:
            # 测试关闭demo
            self.website_manage.demo_model = False
            self.website_manage.save()

    def test_register(self):
        """
        注册涉及两种情况：
        一种是开放注册，注册完成后自动登录
        一种是没开放注册
        """
        # 默认情况是关闭register的
        # 先测试没开放register的情况
        email = self._create_email()
        user_dict = {
            'username': uuid4().hex[:8],
            'password': uuid4().hex[:8],
            'first_name': uuid4().hex[:4],
            'last_name': uuid4().hex[:4],
            'phone': uuid4().hex[:11],
            'email': email,
        }
        c = Client()
        res_1 = c.post(self._restful_url('register'), user_dict, self.json_content_type)
        self._check_bad_request(res_1)
        d = self._base_get_user_check(c)
        self._not_login_check(d)
        try:
            # 开启register再测试
            self.website_manage.open_register = True
            self.website_manage.save()
            res_2 = c.post(self._restful_url('register'), user_dict, self.json_content_type)
            self._base_response_check(res_2)
            u = User.objects.get(email=email)
            d = self._base_get_user_check(c)
            self._user_login_check(d, u)
        finally:
            # 测试关闭register
            self.website_manage.open_register = False
            self.website_manage.save()
