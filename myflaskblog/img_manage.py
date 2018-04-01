#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
文章上传图片处理
'''

# 引入数据库
from myflaskblog import db
from myflaskblog.models import Article, Img

# 导入html解析器，解析富文本
from bs4 import BeautifulSoup

# 引入必要模块
import os
from flask import current_app


# 添加文章时为img数据库的相应添加文章id
def img_add_article_id(article, html):
    soup = BeautifulSoup(html, 'lxml')
    all_img = soup.find_all('img')
    for img in all_img:
        img_url = img.get('src')
        filename = img_url.rsplit('/', 1)[1]
        db_img = Img.query.filter_by(img_name=filename).first()
        db_img.article_id = article
        db.session.commit()


# 修改文章时处理图片
def img_change_article_id(article, html):
    old_imgs = Img.query.filter_by(article_id=article).all()
    soup = BeautifulSoup(html, 'lxml')
    all_img = soup.find_all('img')
    new_img_name = []
    for img in all_img:
        img_url = img.get('src')
        filename = img_url.rsplit('/', 1)[1]
        new_img_name.append(filename)
        db_img = Img.query.filter_by(img_name=filename).first()
        db_img.article_id = article
        db.session.commit()
    for old_img in old_imgs:
        upload_folder = current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'] + 'article_img/'
        if old_img.img_name not in new_img_name:
            os.remove(upload_folder + old_img.img_name)
            db.session.delete(old_img)
