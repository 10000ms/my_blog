# -*- coding: utf-8 -*-
from django.db import models


class Tab(models.Model):

    title = models.CharField('标签', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
