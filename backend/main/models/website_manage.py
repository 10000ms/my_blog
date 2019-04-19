# -*- coding: utf-8 -*-
from django.db import models

from utils.model_str import str_for_model


class WebsiteManage(models.Model):

    about_me = models.TextField('关于我页面内容')
    website_name = models.CharField('网站名', max_length=10)
    ICP_number = models.CharField('备案号', max_length=20)
    website_image = models.CharField('网站头像', max_length=256)
    ad_1 = models.URLField('主页侧栏图片1')
    ad_1_url = models.URLField('主页侧栏图片1广告url')
    ad_2 = models.URLField('主页侧栏图片2')
    ad_2_url = models.URLField('主页侧栏图片2广告url')
    github = models.URLField('Github地址')
    email = models.EmailField('邮箱地址')
    friendship_link = models.CharField('友情链接地址', max_length=2000)

    open_register = models.BooleanField('是否开放注册', default=False)
    demo_model = models.BooleanField('是否开放demo模式', default=False)

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-id']
