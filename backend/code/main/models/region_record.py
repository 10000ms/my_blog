# -*- coding: utf-8 -*-
from django.db import models

from utils.model_str import str_for_model
from ..manager import region_record


class RegionRecord(models.Model):

    date = models.DateField('日期', auto_now=True)
    region = models.ForeignKey('Region', blank=True, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField('统计', default=0)

    objects = region_record.RegionRecordManager()

    def __str__(self):
        return str_for_model(self)
