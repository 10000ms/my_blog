#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
配置模块
'''


class Config_Default(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config_Default):
    DATABASE_URI = 'mysql://user@localhost/foo'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config_Default):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class TestingConfig(Config_Default):
    TESTING = True


config = {
    'config': DevelopmentConfig,
}