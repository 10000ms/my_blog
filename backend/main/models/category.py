# -*- coding: utf-8 -*-
from django.db import models

from utils.model_str import str_for_model


class Category(models.Model):

    title = models.CharField('分类', max_length=30)
    father_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-id']
