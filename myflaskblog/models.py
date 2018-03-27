#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
数据库模型模块
'''

# 导入模型模块
from myflaskblog import db

# 导入加密用包
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 导入datetime时间包
from datetime import datetime

# 导入flask_login的UserMixin类，让login正确工作
from flask_login import UserMixin

# 导入必要模块
from myflaskblog import app
from flask import current_app

# 用户模型
class User(db.Model, UserMixin):
    '''
    创建类的时候继承UserMixin ,有一些用户相关属性 
 
    * is_authenticated ：是否被验证 
    * is_active ： 是否被激活 
    * is_anonymous : 是否是匿名用户 
    * get_id() : 获得用户的id，并转换为 Unicode 类型 
    
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))
    username = db.Column(db.String(80))
    email = db.Column(db.String(32))
    is_admin = db.Column(db.Integer)
    create_datetime = db.Column(db.DateTime)
    confirmed = db.Column(db.Boolean, default=False)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    articles = db.relationship('Article', backref='user', lazy='dynamic')

    def __init__(self, account, password_hash, username, email, is_admin=0):
        self.account = account
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password_hash)
        self.create_datetime = datetime.now()
        self.is_admin = is_admin

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 注意重启app的时候SECRET_KEY会重置
    def generate_token(self, function_module, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        if function_module == 'confirm':
            fm_name = 'c'
        elif function_module == 'resetemail':
            fm_name = 're'
        elif function_module == 'resetpassword':
            fm_name = 'rp'
        return s.dumps({fm_name: self.id})

    def check_token(self, token, function_module):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if function_module == 'confirm':
            fm_name = 'c'
            if data.get(fm_name) != self.id:
                return False
            self.confirmed = True
            db.session.add(self)
            return True
        elif function_module == 'resetemail':
            fm_name = 're'
            if data.get(fm_name) != self.id:
                return False
            return True
        elif function_module == 'resetpassword':
            fm_name = 'rp'
            if data.get(fm_name) != self.id:
                return False
            return True


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
    comments = db.relationship('Comment', backref='article', lazy='dynamic')

    def __init__(self, title, keyword, description, content, user_id):
        self.create_datetime = datetime.now()
        self.title = title
        self.keyword = keyword
        self.description = description
        self.content = content
        self.user_id = user_id

        # TODO:正确的处理新文章简历的模块


# 评论模块
class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True)
    create_datetime = db.Column(db.DateTime)
    title = db.Column(db.String(128))
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def __init__(self, title, comment, user_id, article_id):
        self.create_datetime = datetime.now()
        self.title = title
        self.comment = comment
        self.user_id = user_id
        self.article_id = article_id

        # TODO:正确的处理评论模块

