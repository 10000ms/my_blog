# -*- coding: utf-8 -*-
from django.db import models

from utils.model_str import str_for_model

from .blog import Blog


class Category(models.Model):

    title = models.CharField('分类', max_length=30)
    father_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    @property
    def count(self):
        return Blog.objects.count_category(self.id)

    def category_index(self):
        """
        计算排序数字，方便后面进行排序
        """
        model = self
        index = model.pk
        father = model.father_category
        while father:
            index = index * 0.1 + father.id
            model = model.father_category
            father = model.father_category
        return index

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-id']
