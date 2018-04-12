# -*- coding: utf-8 -*-
"""
    myflaskblog.img_manage
    ~~~~~~~~~

    图片管理模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 引入数据库
from myflaskblog import db, app
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
            db.session.commit()


# 定时清理图片
def clear_useless_img():
    if not app.config['APSCHEDULER_LOCK']:
        app.config.update(APSCHEDULER_LOCK=True)
        need_clear_imgs = Img.query.filter_by(article_id=None).all()
        upload_folder = app.static_folder + app.config['IMG_UPLOAD_FOLDER'] + 'article_img/'
        for need_clear_img in need_clear_imgs:
            os.remove(upload_folder + need_clear_img.img_name)
            db.session.delete(need_clear_img)
            db.session.commit()
        app.config.update(APSCHEDULER_LOCK=False)


def get_profile_photo_folder():
    return current_app.config['IMG_UPLOAD_FOLDER'].split('/', 1)[1] + 'profile_photo/'