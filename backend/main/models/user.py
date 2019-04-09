# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.model_str import str_for_model


class User(AbstractUser):

    phone = models.CharField('电话号码', max_length=30, blank=True)
    is_author = models.BooleanField('是否是作者', default=False)

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-id']