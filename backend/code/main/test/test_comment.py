# -*- coding: utf-8 -*-
from uuid import uuid4

from ._base import BaseModelTest
from ..models.comment import Comment


class TestComment(BaseModelTest):

    item_url = '/api/comment/'

    comment_key = [
        'id',
        'title',
        'content',
        'creator',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.blog = None

    def setUp(self):
        super().setUp()
        # 添加一个原始数据，保证数据库内有blog
        self.blog = self._add_blog_to_db(uuid4().hex[:6])
        self._add_comment_to_db()

    def _add_comment_to_db(self, title=uuid4().hex[:6], user=None):
        if not user:
            user = self.user
        c = Comment.objects.create(
            title=title,
            creator=user,
            blog=self.blog,
            content=uuid4().hex,
        )
        return c

    def test_get_comment(self):
        res = self.not_login_user_client.get(self._restful_url('blog', id=self.blog.id))
        self.base_response_check(res)
        single_comment = res.json()['data'][0]
        self.check_key_in_dict(self.comment_key, single_comment)

    def _need_create_change_check(self, need, response, title, creator=None):
        """
        因为create和change的need检查逻辑部分是一样的，所以放在这个方法里面
        :param need: 是否需要增加或者修改
        :type need: bool
        :param response: 原始返回
        :param title: 检查的comment title
        """
        c = Comment.objects.filter(title=title)
        if need:
            self.base_response_check(response)
            self.assertTrue(c.exists())
            self.assertEqual(c[0].creator.id, creator.id)
        else:
            self.check_not_auth(response)
            self.assertFalse(c.exists())

    def create_comment_test_data(self, title=uuid4().hex[:6]):
        return {
            'blog_pk': self.blog.id,
            'title': title,
            'content': uuid4().hex,
        }

    def _base_create_test(self, client, user=None, need_create=False):
        """
        基础的创建comment检测
        """
        title = uuid4().hex[:6]
        t = self.create_comment_test_data(title)
        res = client.post(self._restful_url(), t, self.json_content_type)
        self._need_create_change_check(need_create, res, t['title'], user)

    def test_user_create_comment(self):
        self._base_create_test(self.user_client, self.user, True)

    def test_not_login_user_create_comment(self):
        self._base_create_test(self.not_login_user_client)

    def _base_change_test(self, client, user, need_change=False):
        """
        基础的修改comment检测
        """
        temp_comment = self._add_comment_to_db(user=user)
        # 再生成一个用于修改的信息
        title = uuid4().hex[:8]
        t = self.create_comment_test_data(title)
        res = client.put(self._restful_url(temp_comment.id), t, self.json_content_type)
        self._need_create_change_check(need_change, res, title, user)

    def test_user_change_comment(self):
        """
        因为用户是可以修改自己的comment而不能修改其他人的comment的，所以这里有两个测试
        """
        # 修改其他人的comment
        self._base_change_test(self.user_client, self.superuser)
        # 修改自己的comment
        self._base_change_test(self.user_client, self.user, True)

    def test_not_login_user_change_comment(self):
        self._base_change_test(self.not_login_user_client, self.user)

    def _base_delete_test(self, client, user, need_delete=False):
        """
        基础的删除comment检测
        """
        # 先创建一个新的comment
        title = uuid4().hex[:8]
        temp_title = self._add_comment_to_db(title=title, user=user)
        res = client.delete(self._restful_url(temp_title.id))
        c = Comment.objects.filter(title=title)
        if need_delete:
            self.check_success_response(res)
            self.assertFalse(c.exists())
        else:
            self.check_not_auth(res)
            self.assertTrue(c.exists())

    def test_user_delete_comment(self):
        """
        因为用户是可以删除自己的comment而不能修改其他人的comment的，所以这里有两个测试
        """
        # 修改其他人的comment
        self._base_delete_test(self.user_client, self.superuser)
        # 修改自己的comment
        self._base_delete_test(self.user_client, self.user, True)

    def test_not_login_user_delete_comment(self):
        self._base_delete_test(self.not_login_user_client, self.user)
