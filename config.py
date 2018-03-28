#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
配置模块
'''

import os, sys
from flask import current_app


class Config_Default(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config_Default):
    DATABASE_URI = 'mysql://user@localhost/foo'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config_Default):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/test?charset=utf8'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #跟踪修改，耗费资源，后期将会取消，False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True  # 使用本地的bootstrap源
    IS_DEVELOPMENT = True  # 自定义值，检查是否出于开发配置环境
    SECRET_KEY = os.urandom(24)  # 配置密匙值，session、cookies及部分其他应用会用到
    PROJECT_PATH = sys.path[0]  # 项目路径

    FLASKY_MAIL_SUBJECT_PREFIX = '1000ms'  # 邮件标题名前缀
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')  # 发邮件的人

    MAIL_SERVER = 'smtp.qq.com'  # 发送邮件服务器
    MAIL_PORT = 587  # 使用端口
    MAIL_USE_TLS = True  # 启用安全套接层TLS协议
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # 邮箱登陆用户名，从环境变量中获取
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # 邮箱登陆密码，从环境变量中获取

    IMG_UPLOAD_FOLDER = '/img/'  # 文件上传相关，目录配置
    IMG_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])  # 文件上传相关，允许文件名


class TestingConfig(Config_Default):
    TESTING = True


config = {
    'config': DevelopmentConfig,
}