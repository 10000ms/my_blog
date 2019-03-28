# -*- coding: utf-8 -*-
from django.db import models


class Blog(models.Model):

    title = models.CharField('标题', max_length=256)
    author = models.CharField('作者', max_length=256)
    create_time = models.DateTimeField('创建时间')
    last_change_time = models.DateTimeField('最后修改', auto_now_add=True, editable=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.DO_NOTHING)
    tabs = models.ManyToManyField('Tab')
    brief = models.CharField('简介', max_length=256)
    content = models.TextField('正文')
    read_count = models.IntegerField('阅读数')
    like_count = models.IntegerField('喜欢数')

    def __str__(self):
        return self.title
