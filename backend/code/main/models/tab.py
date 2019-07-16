from django.db import models

from utils.model_str import str_for_model

from .blog import Blog


class Tab(models.Model):

    title = models.CharField('标签', max_length=30)

    @property
    def count(self):
        return Blog.objects.count_tabs(self.id)

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['id']
