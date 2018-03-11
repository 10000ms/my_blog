#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
数据库模型模块
'''

# 导入模型模块
from myflaskblog import db

# 导入md5包
import hashlib

# 导入datetime时间包
from datetime import datetime

# 用户模型
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
    is_admin = db.Column(db.Integer)
    create_datetime = db.Column(db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = hashlib.md5(str(password).encode('utf-8')).hexdigest()
        self.create_datetime = datetime.now()

        # TODO:密码使用更合理的方式进行保存，+salt等。


# 常规配置模块
class Config(db.Model):
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True)


# blog文章模块
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    create_datetime = db.Column(db.DateTime)
    title = db.Column(db.String(128))
    keyword = db.Column(db.String(250))
    description = db.Column(db.String(250))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, keyword, description, content):
        self.create_datetime = datetime.now()
        self.title = title
        self.keyword = keyword
        self.description = description
        self.content = content

        # TODO:正确的处理新文章简历的模块


# 评论模块
class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
    create_datetime = db.Column(db.DateTime)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def __init__(self, title, content):
        self.create_datetime = datetime.now()
        self.title = title
        self.content = content

        # TODO:正确的处理评论模块

