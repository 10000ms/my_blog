# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):

    account = models.CharField('标题', max_length=30)
    password = models.CharField('作者', max_length=30)
    username = models.DateTimeField('创建时间')
    phone = models.CharField('最后修改', max_length=30)
    email = models.EmailField('Email地址')
    superuser = models.BooleanField('是否是超级用户')
    author = models.BooleanField('是否是作者')

    def __str__(self):
        return self.username
