#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
用户页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/')
def index_page():
    return 'this is user page'
