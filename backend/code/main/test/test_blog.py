from uuid import uuid4

from ._base import BaseModelTest
from ..models.blog import Blog


class TestBlog(BaseModelTest):

    item_url = '/api/blog/'

    blog_key = [
        'id',
        'title',
        'creator',
        'author',
        'create_time',
        'last_change_time',
        'category',
        'tabs',
        'brief',
        'content',
        'read_count',
        'like_count',
        'is_recommend',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tab = None
        self.category = None
        self.blog = None

    def setUp(self):
        super().setUp()
        # 添加一些初始辅助数据
        self.tab = self._add_tab_to_db()
        self.category = self._add_category_to_db()
        self.blog = self._add_blog_to_db(uuid4().hex[:6])

    def _base_get_blog_check(self, client):
        """
        基础的获取blog检测
        """
        self.today_record.refresh_from_db()
        old_day_count = self.today_record.read_count
        old_blog_count = self.blog.read_count
        res = client.get(self._restful_url(self.blog.id))
        self._base_response_check(res)
        data = res.json()['data']
        # 只测试其中一个即可
        self.blog.refresh_from_db()
        self.today_record.refresh_from_db()
        self._check_key_in_dict(self.blog_key, data)
        self.assertGreater(self.blog.read_count, old_blog_count)
        self.assertGreater(self.today_record.read_count, old_day_count)

    def test_user_get_blog(self):
        self._base_get_blog_check(self.user_client)

    def test_superuser_get_blog(self):
        self._base_get_blog_check(self.superuser_client)

    def test_not_login_user_get_blog(self):
        self._base_get_blog_check(self.not_login_user_client)

    def _need_create_change_check(self, need, response, title, creator=None):
        """
        因为create和change的need检查逻辑部分是一样的，所以放在这个方法里面
        :param need: 是否需要增加或者修改
        :type need: bool
        :param response: 原始返回
        :param title: 检查的 blog title
        """
        c = Blog.objects.filter(title=title)
        if need:
            self._base_response_check(response)
            self.assertTrue(c.exists())
            self.assertEqual(c[0].creator.id, creator.id)
        else:
            self._check_not_auth(response)
            self.assertFalse(c.exists())

    def _base_create_blog_check(self, client, create=None, need_create=False):
        """
        基础的创建blog检测
        """
        title = uuid4().hex[:6]
        create_dict = self._create_blog_dict(title)
        res = client.post(self._restful_url(), create_dict, self.json_content_type)
        self._need_create_change_check(need_create, res, title, create)

    def test_user_create_blog(self):
        self._base_create_blog_check(self.user_client)

    def test_superuser_create_blog(self):
        self._base_create_blog_check(self.superuser_client, self.superuser, True)

    def test_not_login_user_create_blog(self):
        self._base_create_blog_check(self.not_login_user_client)

    def _create_blog_dict(self, title):
        return {
            'title': title,
            'author': uuid4().hex[:6],
            'brief': uuid4().hex,
            'content': uuid4().hex,
            'tabs_pk': [self.tab.id],
            'category_pk': self.category.id,
        }

    def _base_change_blog_check(self, client, create=None, need_change=False):
        """
        基础的修改blog检测
        """
        old_title = uuid4().hex[:6]
        new_title = uuid4().hex[:8]
        b = self._add_blog_to_db(old_title)
        res = client.put(self._restful_url(b.id), self._create_blog_dict(new_title), self.json_content_type)
        self._need_create_change_check(need_change, res, new_title, create)

    def test_user_change_blog(self):
        self._base_change_blog_check(self.user_client)

    def test_superuser_change_blog(self):
        self._base_change_blog_check(self.superuser_client, self.superuser, True)

    def test_not_login_user_change_blog(self):
        self._base_change_blog_check(self.not_login_user_client)

    def _base_delete_blog_check(self, client, need_delete=False):
        """
        基础的删除blog检测
        """
        # 先创建一个新的blog
        title = uuid4().hex[:6]
        b = self._add_blog_to_db(title)
        res = client.delete(self._restful_url(b.id))
        c = Blog.objects.filter(title=title)
        if need_delete:
            self._check_success_response(res)
            self.assertFalse(c.exists())
        else:
            self._check_not_auth(res)
            self.assertTrue(c.exists())

    def test_user_delete_blog(self):
        self._base_delete_blog_check(self.user_client)

    def test_superuser_delete_blog(self):
        self._base_delete_blog_check(self.superuser_client, True)

    def test_not_login_user_delete_blog(self):
        self._base_delete_blog_check(self.not_login_user_client)

    def test_like(self):
        old_day_like = self.today_record.like_count
        old_blog_like = self.blog.like_count
        self.not_login_user_client.post(self._restful_url('heart'), {'id': self.blog.id}, self.json_content_type)
        self.blog.refresh_from_db()
        self.today_record.refresh_from_db()
        self.assertEqual(self.blog.like_count, old_blog_like + 1)
        self.assertEqual(self.today_record.like_count, old_day_like + 1)
