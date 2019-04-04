# -*- coding: utf-8 -*-
from django.db import models


class BlogManager(models.Manager):

    def index_info(self):
        return super().all()[:10]
