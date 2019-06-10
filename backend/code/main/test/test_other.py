# -*- coding: utf-8 -*-
from ._base import BaseModelTest


class TestOther(BaseModelTest):
    """
    其他测试

    现在只包含生成环境下不应该被暴露的url测试，使用最高权限的超级管理员类来测试
    """

    def test_test_url(self):
        """
        正式环境下test的url应该被关闭
        """
        res = self.superuser_client.get('/api/test/')
        self._check_not_found(res)

    def test_admin_url(self):
        """
        正式环境下admin的url应该被关闭
        """
        res = self.superuser_client.get('/admin/')
        self._check_not_found(res)

    def test_api_auth_url(self):
        """
        正式环境下api-auth的url应该被关闭
        """
        res = self.superuser_client.get('/api-auth/')
        self._check_not_found(res)
