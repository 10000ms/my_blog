# -*- coding: utf-8 -*-
from django.db import models

from ..middleware.current_user import get_current_user
from ..manager import blog
from utils.model_str import str_for_model
from utils.es import ESControl


class Blog(models.Model):

    title = models.CharField('标题', max_length=256)
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.PROTECT, default=get_current_user)
    author = models.CharField('作者', max_length=256)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    last_change_time = models.DateTimeField('最后修改', auto_now=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    tabs = models.ManyToManyField('Tab')
    brief = models.CharField('简介', max_length=256)
    content = models.TextField('正文')
    read_count = models.IntegerField('阅读数', default=0)
    like_count = models.IntegerField('喜欢数', default=0)
    is_recommend = models.BooleanField('是否推荐', default=False)

    objects = blog.BlogManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        重写save方法，支持es搜索功能
        """
        res = super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )
        es = ESControl()
        es_body = {
            'title': self.title,
            'author': self.author,
            'create_time': self.create_time,
            'last_change_time': self.last_change_time,
            'brief': self.brief,
            'content': self.content,
        }
        es.update('blog', doc_id=self.id, body=es_body)
        return res

    def delete(self, using=None, keep_parents=False):
        """
        重写delete方法，支持es搜索功能
        """
        i = self.id
        res = super().delete(using=using, keep_parents=keep_parents)
        es = ESControl()
        es.delete('blog', doc_id=i)
        return res

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-create_time']
