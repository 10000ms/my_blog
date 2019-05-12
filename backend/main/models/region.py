# -*- coding: utf-8 -*-
from django.db import models

from utils.model_str import str_for_model


class Region(models.Model):

    province = models.CharField('标题', max_length=10)
    city = models.CharField('标题', max_length=20)

    def __str__(self):
        return str_for_model(self)
