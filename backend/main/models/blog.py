# -*- coding: utf-8 -*-
from django.db import models

from ..middleware.current_user import get_current_user
from .user import User
from ..manager import blog
from utils.model_str import str_for_model


class Blog(models.Model):

    title = models.CharField('标题', max_length=256)
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, default=get_current_user)
    author = models.CharField('作者', max_length=256)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    last_change_time = models.DateTimeField('最后修改', auto_now=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.DO_NOTHING)
    tabs = models.ManyToManyField('Tab')
    brief = models.CharField('简介', max_length=256)
    content = models.TextField('正文')
    read_count = models.IntegerField('阅读数', default=0)
    like_count = models.IntegerField('喜欢数', default=0)
    is_recommend = models.BooleanField('是否推荐', default=False)

    objects = blog.BlogManager()

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-create_time']
