#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
主页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

# 导入模板模块
from flask import render_template

# 导入必要的模块
from myflaskblog.models import User, Article

index = Blueprint('index', __name__)


@index.route('/')
def index_page():
    return render_template("/index/index.html")



