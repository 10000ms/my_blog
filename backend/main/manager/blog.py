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

    def heart(self, blog_id):
        b = self.get(id=blog_id)
        b.like_count += 1
        b.save()

    def add_recommend(self, blog_id):
        b = self.get(id=blog_id)
        b.is_recommend = True
        b.save()

    def cancel_recommend(self, blog_id):
        b = self.get(id=blog_id)
        b.is_recommend = False
        b.save()

    def add_read_count(self, blog_id):
        b = self.get(id=blog_id)
        b.read_count += 1
        b.save()
