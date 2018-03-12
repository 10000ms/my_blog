#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
配置模块
'''

import os


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

class TestingConfig(Config_Default):
    TESTING = True


config = {
    'config': DevelopmentConfig,
}