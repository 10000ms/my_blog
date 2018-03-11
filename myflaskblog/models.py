#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
数据库模型模块
'''

#导入模型模块
from myflaskblog import db


# 用户模型
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
    is_admin = db.Column(db.Integer)
    creata_datetime = db.Column(db.DateTime)

    def __init__(self, username, email):
        self.username = username
        self.email = email


# 常规配置模块
class Config(db.Model):
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True)


# blog文章模块
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)


# 评论模块
class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
