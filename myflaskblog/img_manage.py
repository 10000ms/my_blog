# -*- coding: utf-8 -*-
"""
    myflaskblog.img_manage
    ~~~~~~~~~

    图片管理模块
    对文章，头像的数据库信息进来管理，并删除无用图片
    含定期删除图片功能

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入os包进行文件操作相关
import os
# 导入html解析器，解析富文本
from bs4 import BeautifulSoup

# 导入flask相关的功能
from flask import current_app

# 引入项目，数据库及模型
from myflaskblog import app
from myflaskblog import db
from myflaskblog.models import Img


def img_add_article_id(article, html):
    """
    添加文章时在数据库中为富文本编辑器提前上传的图片信息添加文章id
    方便后面清除没有文章id的图片
    数据库中图片信息已经在图片上传时添加

    :param article: 图片的文章id
    :param html: 文章内容
    :return:
    """
    soup = BeautifulSoup(html, 'lxml')
    all_img = soup.find_all('img')
    for img in all_img:
        img_url = img.get('src')
        filename = img_url.rsplit('/', 1)[1]
        db_img = Img.query.filter_by(img_name=filename).first()
        if db_img:
            db_img.article_id = article
            db.session.commit()


def img_change_article_id(article, html):
    """
    提交修改文章时，数据库中新图片信息增加对应文章id，无用文章旧图片清除

    :param article: 图片的文章id
    :param html: 文章内容
    :return:
    """
    old_imgs = Img.query.filter_by(article_id=article).all()
    soup = BeautifulSoup(html, 'lxml')
    all_img = soup.find_all('img')
    new_img_name = []
    for img in all_img:
        img_url = img.get('src')
        filename = img_url.rsplit('/', 1)[1]
        db_img = Img.query.filter_by(img_name=filename).first()
        if db_img:
            new_img_name.append(filename)
            db_img.article_id = article
            db.session.commit()
    for old_img in old_imgs:
        upload_folder = current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'] + 'article_img/'
        if old_img.img_name not in new_img_name:
            os.remove(upload_folder + old_img.img_name)
            db.session.delete(old_img)
            db.session.commit()


def article_delete(article):
    """
    文章删除时清理对应的图片

    :param article: 被删除的文章id
    :return:
    """
    need_clean_imgs = Img.query.filter_by(article_id=article).all()
    if need_clean_imgs:
        for need_clean_img in need_clean_imgs:
            os.remove(get_article_img_folder() + need_clean_img.img_name)


def clear_useless_img():
    """
    定期清理图片功能，先获取锁，防止同时执行错误，然后进行查找没有文章id的图片进行清理

    :return:
    """
    if not app.config['APSCHEDULER_LOCK']:
        app.config.update(APSCHEDULER_LOCK=True)
        need_clear_imgs = Img.query.filter_by(article_id=None).all()
        for need_clear_img in need_clear_imgs:
            os.remove(get_article_img_folder() + need_clear_img.img_name)
            db.session.delete(need_clear_img)
            db.session.commit()
        app.config.update(APSCHEDULER_LOCK=False)


def get_profile_photo_folder():
    """
    用户头像上传目录的url

    :return: 上传目录url
    """
    return current_app.config['IMG_UPLOAD_FOLDER'].split('/', 1)[1] + 'profile_photo/'


def get_article_img_folder():
    """
    文章图片上传目录

    :return: 上传目录
    """
    return current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'] + 'article_img/'
