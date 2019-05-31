# -*- coding: utf-8 -*-
from uuid import uuid4

from ._base import BaseModelTest
from ..models.tab import Tab


class TestTab(BaseModelTest):

    tab_url = '/api/tab/'

    tab_data = {
        'title': '测试标签{}'.format(uuid4().hex[:6]),
    }

    tab_key = [
        'id',
        'title',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_tab_1 = None
        self.test_tab_2 = None

    def setUp(self):
        super().setUp()
        # 添加一些原始数据
        self.test_tab_1 = Tab.objects.create(title='测试标签1')
        self.test_tab_2 = Tab.objects.create(title='测试标签2')

    def _base_get_tab_check(self, response):
        self.base_response_check(response)
        data = response.json()['data']
        self.assertIsInstance(data, list)
        # 只测试其中一个即可
        self.check_key_in_dict(self.tab_key, data[0])

    def test_user_get_tab(self):
        res = self.user_client.get(self.tab_url)
        self._base_get_tab_check(res)

    def test_superuser_get_tab(self):
        res = self.superuser_client.get(self.tab_url)
        self._base_get_tab_check(res)

    def test_not_login_user_get_tab(self):
        res = self.not_login_user_client.get(self.tab_url)
        self._base_get_tab_check(res)

    def test_user_create_tab(self):
        res = self.user_client.post(self.tab_url, self.tab_data, self.json_content_type)
        self.check_not_auth(res.status_code)

    def test_superuser_create_tab(self):
        res = self.superuser_client.post(self.tab_url, self.tab_data, self.json_content_type)

    def test_not_login_user_create_tab(self):
        res = self.not_login_user_client.post(self.tab_url, self.tab_data, self.json_content_type)
        self.check_not_auth(res.status_code)

    def test_user_change_tab(self):
        pass

    def test_superuser_change_tab(self):
        pass

    def test_not_login_user_change_tab(self):
        pass

    def test_user_delete_tab(self):
        pass

    def test_superuser_delete_tab(self):
        pass

    def test_not_login_user_delete_tab(self):
        pass
