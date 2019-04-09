# -*- coding: utf-8 -*-
from django.db import models


class BlogManager(models.Manager):

    def index_info(self):
        return self.all()[:10]

    def recommend(self):
        return self.filter(is_recommend=True)[:10]
