# -*- coding: utf-8 -*-
from uuid import uuid4

from ._base import BaseModelTest
from ..models.website_manage import WebsiteManage


class TestWebsiteManage(BaseModelTest):

    item_url = '/api/website-manage/'

    def _base_create_website_manage_check(self, client):
        """
        基础创建website_manage测试
        """
        res = client.post(self._restful_url(), {}, self.json_content_type)
        self.check_not_auth(res)

    def test_user_create_website_manage(self):
        self._base_create_website_manage_check(self.user_client)

    def test_not_login_user_create_website_manage(self):
        self._base_create_website_manage_check(self.not_login_user_client)

    def _base_delete_website_manage_check(self, client):
        """
        基础删除website_manage测试
        """
        res = client.delete(self._restful_url(self.website_manage.id))
        self.check_not_auth(res)

    def test_user_delete_website_manage(self):
        self._base_delete_website_manage_check(self.user_client)

    def test_not_login_user_delete_website_manage(self):
        self._base_delete_website_manage_check(self.not_login_user_client)

    def _base_change_website_manage_check(self, client, superuser=False):
        """
        基础删除website_manage测试
        """
        e = '{}@admin.com'.format(uuid4().hex)
        res = client.put(self._restful_url(
            self.website_manage.id),
            {'email': e},
            self.json_content_type
        )
        if superuser:
            self.check_success_response(res)
            w = WebsiteManage.objects.all()[:1]
            self.assertEqual(e, w.email)
        else:
            self.check_not_auth(res)

    def test_user_change_website_manage(self):
        self._base_change_website_manage_check(self.user_client)

    def test_not_login_user_change_website_manage(self):
        self._base_change_website_manage_check(self.not_login_user_client)

    def test_superuser_change_website_manage(self):
        self._base_change_website_manage_check(self.user_client)
