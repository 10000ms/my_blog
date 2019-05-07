# -*- coding: utf-8 -*-
from django.db import models


class BlogManager(models.Manager):

    def recommend(self):
        return self.filter(is_recommend=True)[:10]

    def query_tab(self, tab_id):
        return self.filter(tabs__id__contains=tab_id)

    def count_tabs(self, tab_id):
        return self.filter(tabs__id__contains=tab_id).count()

    def query_category(self, category_id):
        return self.filter(category__id=category_id)

    def count_category(self, category_id):
        return self.filter(category__id=category_id).count()
