#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
路由模块
'''

from myflaskblog import app


@app.route("/")
def index():
    return "Hello World!"


@app.route("/user")
def index():
    '''
    用户信息
    '''
    pass


@app.route("/admin")
def index():
    '''
    后台管理信息
    '''
    pass


@app.route("/article")
def index():
    '''
    博文
    '''
    pass