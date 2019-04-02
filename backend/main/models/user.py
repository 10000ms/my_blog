# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone = models.CharField('电话号码', max_length=30)
    is_author = models.BooleanField('是否是作者', default=False)
