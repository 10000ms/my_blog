# -*- coding: utf-8 -*-
from django.db import models

from utils.model_str import str_for_model


class Tab(models.Model):

    title = models.CharField('标签', max_length=30)

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-id']
