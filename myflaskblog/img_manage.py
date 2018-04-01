#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
文章上传图片处理
'''

# 引入数据库
from myflaskblog import db
from myflaskblog import models

# 导入html解析器，解析富文本
from bs4 import BeautifulSoup
import lxml


# 添加文章时为img数据库的相应添加文章id
def img_add_article_id(article, html):
    soup = BeautifulSoup(html, lxml)
    all_img = soup.find_all('img')
    for img in all_img:
        pass
