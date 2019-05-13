# -*- coding: utf-8 -*-
from django.db import models

from utils.model_str import str_for_model
from ..manager import region


class Region(models.Model):

    province = models.CharField('省份', max_length=10)
    city = models.CharField('城市', max_length=20)
    city_id = models.IntegerField('city_id', default=0)
    x = models.FloatField('x', default=0.0)
    y = models.FloatField('y', default=0.0)

    objects = region.RegionManager()

    def __str__(self):
        return str_for_model(self)
