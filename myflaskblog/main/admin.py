#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
管理页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route('/')
def index_page():
    return 'this is admin page'