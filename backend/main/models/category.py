# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):

    title = models.CharField('分类', max_length=30)
    father_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
