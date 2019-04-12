# -*- coding: utf-8 -*-
from django.db import models


class BlogManager(models.Manager):

    def recommend(self):
        return self.filter(is_recommend=True)[:10]
