# -*- coding: utf-8 -*-
"""
    myflaskblog.models
    ~~~~~~~~~

    数据库模型类模块
    网站所需要用到的mysql数据库的所有模型
    内含：
    1.网站用户模型
    2.网站设置模型
    3.blog文章模型
    4.博文评论模型
    5.文章图片模型

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入加密用包
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 导入datetime时间包
from datetime import datetime

# 导入flask_login的UserMixin类，让login正确工作
from flask_login import UserMixin

# 导入必要模块
from flask import current_app
from myflaskblog import db


class User(db.Model, UserMixin):
    """
    网站用户模型

    创建类的时候继承UserMixin ,有一些用户相关属性 
 
    * is_authenticated ：是否被验证 
    * is_active ： 是否被激活 
    * is_anonymous : 是否是匿名用户 
    * get_id() : 获得用户的id，并转换为 Unicode 类型 
    
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))
    username = db.Column(db.String(80))
    profile_photo = db.Column(db.String(128), default='Default.jpg')
    email = db.Column(db.String(32))
    is_admin = db.Column(db.Integer)
    create_datetime = db.Column(db.DateTime)
    confirmed = db.Column(db.Boolean, default=False)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    articles = db.relationship('Article', backref='user', lazy='dynamic')

    def __init__(self, account, password_hash, username, email, is_admin=False, confirmed=False):
        """
        增加用户功能

        :param account: 用户帐号
        :param password_hash: 用户密码hash值
        :param username: 用户名
        :param email: 用户email
        :param is_admin: 管理权限
        :param confirmed: 邮箱认证
        """
        self.account = account
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password_hash)
        self.create_datetime = datetime.now()
        self.is_admin = is_admin
        self.confirmed = confirmed

    def change_password(self, new_password):
        """
        修改密码，提交至数据库

        :param new_password: 新密码
        :return:
        """
        self.password_hash = generate_password_hash(new_password)
        db.session.commit()

    @property
    def password(self):
        """
        防止password被访问

        :return:
        """
        raise AttributeError('password is not a readable attribute')

    def verify_password(self, password):
        """
        认证密码

        :param password: 要认证的密码
        :return:
        """
        return check_password_hash(self.password_hash, password)

    def generate_token(self, function_module, expiration=3600):
        """
        生成邮箱认证token
        注意重启app的时候SECRET_KEY会重置

        :param function_module: 功能名
        :param expiration: 过期时间
        :return:
        """
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        if function_module == 'confirm':
            fm_name = 'c'
        elif function_module == 'resetpassword':
            fm_name = 'rp'
        return s.dumps({fm_name: self.id})

    def check_token(self, token, function_module):
        """
        模型类中的认证token检查，并激活

        :param token: 要认真的token
        :param function_module: 功能名
        :return:
        """
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
            db.session.commit()
            return True
        elif function_module == 'resetpassword':
            fm_name = 'rp'
            if data.get(fm_name) != self.id:
                return False
            return True


class Config(db.Model):
    """
    网站设置模型
    """
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(128))
    value = db.Column(db.String(128))

    def __init__(self, item, value):
        self.item = item
        self.value = value


class Article(db.Model):
    """
    blog文章模型
    """
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    create_datetime = db.Column(db.DateTime)
    title = db.Column(db.String(128))
    keyword = db.Column(db.String(250))
    description = db.Column(db.Text)
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


class Comment(db.Model):
    """
    博文评论模型
    """
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


class Img(db.Model):
    """
    文章图片模型，储存图片信息，不储存图片
    """
    __tablename__ = 'Img'
    id = db.Column(db.Integer, primary_key=True)
    create_datetime = db.Column(db.DateTime)
    img_name = db.Column(db.String(128))
    article_id = db.Column(db.Integer, default=None)

    def __init__(self, img_name, article_id=None):
        self.create_datetime = datetime.now()
        self.img_name = img_name
        self.article_id = article_id

