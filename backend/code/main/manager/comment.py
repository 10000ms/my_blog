# -*- coding: utf-8 -*-
from django.db import models


class CommentManager(models.Manager):

    def comment_from_blog(self, blog_id):
        return self.filter(blog__id=blog_id)
