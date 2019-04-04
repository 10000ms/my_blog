# -*- coding: utf-8 -*-
from django.db import models

from .user import User
from .blog import Blog


class Comment(models.Model):

    title = models.CharField('标题', max_length=256)
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.DO_NOTHING)
    content = models.TextField('评论')

    def __str__(self):
        return self.title
