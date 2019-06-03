# -*- coding: utf-8 -*-
from uuid import uuid4

from django.test import (
    TestCase,
    Client,
)

from ..models import (
    user,
    website_manage,
)


class BaseModelTest(TestCase):

    superuser = None
    user = None

    user_client = None
    superuser_client = None
    not_login_user_client = None

    user_username = 'user123'
    user_password = '123456'

    superuser_username = 'admin123'
    superuser_password = '123456'

    base_response_key = ['code', 'data', 'msg']

    json_content_type = 'application/json'

    item_url = ''

    website_manage_data_key = [
        'ICP_number',
        'ad_1',
        'ad_1_url',
        'ad_2',
        'ad_2_url',
        'demo_model',
        'email',
        'friendship_link',
        'github',
        'open_register',
        'website_image',
        'website_name',
    ]

    website_manage = None

    @classmethod
    def setUpTestData(cls):
        """
        重写方法增加初始信息创建
        """
        # 创建用户
        cls.superuser = user.User.objects.create_superuser(
            cls.superuser_username,
            'admin123@admin.com',
            cls.superuser_password,
            phone=uuid4().hex[:11],
        )
        cls.user = user.User.objects.create_user(
            cls.user_username,
            'user123@admin.com',
            cls.user_password,
            phone=uuid4().hex[:11],
        )
        # 创建website_manage
        old_website_manage = website_manage.WebsiteManage.objects.all()
        if not old_website_manage.exists():
            cls.website_manage = website_manage.WebsiteManage.objects.create(
                website_name='测试',
                ICP_number='测试123456',
                website_image='https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg',
                ad_1='https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg',
                ad_1_url='https://www.qq.com/',
                ad_2='https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg',
                ad_2_url='https://www.qq.com/',
                github='https://www.qq.com/',
                email='admin@admin.com',
                friendship_link='http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com'
            )
        # 预先建立client
        cls.user_client = Client()
        cls.user_client.login(username=cls.user_username, password=cls.user_password)
        cls.superuser_client = Client()
        cls.superuser_client.login(username=cls.superuser_username, password=cls.superuser_password)
        cls.not_login_user_client = Client()

    def check_key_in_dict(self, key_list, check_dict):
        """
        检测key是否在dict里面
        :param key_list: 待检测的key的list
        :type key_list: list
        :param check_dict: 待检测的dict
        :type check_dict: dict
        :rtype: bool
        """
        self.assertIsInstance(key_list, list)
        self.assertIsInstance(check_dict, dict)
        res = True
        error_key = []
        for k in key_list:
            if k not in check_dict:
                error_key.append(k)
                res = False
        error_msg = 'key: <{}> of key_list: <{}> not in dict keys: <{}>'\
            .format(error_key, key_list, check_dict.keys())
        self.assertTrue(res, msg=error_msg)

    def check_success_response(self, response):
        """
        返回成功检测，200-299都判断为成功
        :param response: 原始的返回
        """
        s = response.status_code
        self.assertIsInstance(s, int)
        self.assertGreaterEqual(s, 200)
        self.assertLessEqual(s, 299)

    def base_response_check(self, response):
        """
        基本的返回检测
        :param response: 原始的返回
        """
        # 返回码200
        self.check_success_response(response)
        # 对应的数据结果
        self.check_key_in_dict(self.base_response_key, response.json())

    def check_bad_request(self, response):
        """
        检测返回的请求是错误请求
        :param response: 原始的返回
        """
        self.assertEqual(response.status_code, 400)

    def check_not_auth(self, response):
        """
        检测返回的请求是没有对应请求权限
        :param response: 原始的返回
        """
        self.assertEqual(response.status_code, 403)

    def check_not_found(self, response):
        """
        检测返回的请求是找不到
        :param response: 原始的返回
        """
        self.assertEqual(response.status_code, 404)

    def _restful_url(self, item_id=None):
        if item_id:
            return '{}{}/'.format(self.item_url, str(item_id))
        else:
            return self.item_url
