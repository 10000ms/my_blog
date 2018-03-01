#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
主页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

index = Blueprint('index', __name__)


@index.route('/')
def index_page():
    return 'this is index page'
