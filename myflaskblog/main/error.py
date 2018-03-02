#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
出错页面模块
'''

# 导入蓝图模块
from flask import Blueprint

error = Blueprint('error', __name__)


@error.errorhandler(404)
def index_page():
    return '404 Not Found', 404


@error.errorhandler(403)
def index_page():
    return '403 Forbidden', 403


@error.errorhandler(410)
def index_page():
    return '410 Gone', 410


@error.errorhandler(500)
def index_page():
    return '500 Internal Server Error', 500
