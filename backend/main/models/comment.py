# -*- coding: utf-8 -*-
from django.db import models

from ..middleware.current_user import get_current_user
from utils.model_str import str_for_model


class Comment(models.Model):

    title = models.CharField('标题', max_length=256)
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.DO_NOTHING, default=get_current_user)
    blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.DO_NOTHING)
    content = models.TextField('评论')

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-id']
