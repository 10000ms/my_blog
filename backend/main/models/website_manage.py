# -*- coding: utf-8 -*-
from django.db import models


class WebsiteManage(models.Model):

    about_me = models.TextField('关于我页面内容')
    website_name = models.CharField('网站名', max_length=10)
    ICP_number = models.CharField('备案号', max_length=20)
    website_image = models.CharField('网站头像', max_length=256)
    ad_1 = models.CharField('主页侧栏图片1', max_length=256)
    ad_2 = models.CharField('主页侧栏图片2', max_length=256)
    github = models.CharField('Github地址', max_length=256)
    email = models.CharField('邮箱地址', max_length=256)
    Friendship_link = models.CharField('友情链接地址', max_length=2000)

    def __str__(self):
        return self.website_name
