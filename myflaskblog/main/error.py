#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
出错页面模块
'''

# 导入蓝图模块
from flask import Blueprint

# 导入模板模块
from flask import render_template

# error处理模块
# @app.errorhandler(404)
# def error_404_page(error):
#     return '404 Not Found', 404
#
#
# @app.errorhandler(403)
# def error_403_page(error):
#     return '403 Forbidden', 403
#
#
# @app.errorhandler(410)
# def error_410_page(error):
#     return '410 Gone', 410
#
#
# @app.errorhandler(500)
# def error_500_page(error):
#     return '500 Internal Server Error', 500


error_handler = Blueprint('error', __name__)


@error_handler.app_errorhandler(404)
def error_404_page(error):
    return render_template('error/error.html', error_title=404, error_1=4, error_2=0, error_3=4, \
            error_message='该页面不存在'), 404


@error_handler.app_errorhandler(403)
def error_403_page(error):
    return render_template('error/error.html', error_title=403, error_1=4, error_2=0, error_3=3, \
            error_message='资源不可用'), 403


@error_handler.app_errorhandler(401)
def error_401_page(error):
    return render_template('error/error.html', error_title=410, error_1=4, error_2=0, error_3=1, \
            error_message='没有权限'), 401


@error_handler.app_errorhandler(500)
def error_500_page(error):
    return render_template('error/error.html', error_title=500, error_1=5, error_2=0, error_3=0, \
            error_message='服务器内部错误'), 500
