# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task

from ..models.region_record import RegionRecord
from ..models.date_record import DateRecord
from ..models.blog import Blog


@shared_task
def add_ip(ip):
    RegionRecord.objects.add_ip(ip)


@shared_task
def add_read_count(blog_id):
    Blog.objects.add_read_count(blog_id)
    DateRecord.objects.add_read_count()


@shared_task
def add_like_count(blog_id):
    DateRecord.objects.add_like_count()
    Blog.objects.heart(blog_id)


@shared_task
def add_comment_count():
    DateRecord.objects.add_comment_count()
