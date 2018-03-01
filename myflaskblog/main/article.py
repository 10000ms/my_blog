#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
文章页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

article = Blueprint('article', __name__)


@article.route('/')
def index_page():
    return 'this is article page'