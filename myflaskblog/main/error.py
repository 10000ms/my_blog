# -*- coding: utf-8 -*-
"""
    myflaskblog.main.error
    ~~~~~~~~~

    全局错误处理模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入蓝图模块
from flask import Blueprint

# 导入模板模块
from flask import render_template


error_handler = Blueprint('error', __name__)


@error_handler.app_errorhandler(404)
def error_404_page(error):
    return render_template(
        'error/error.html',
        error_title=404,
        error_1=4,
        error_2=0,
        error_3=4,
        error_message='该页面不存在'
    ), 404


@error_handler.app_errorhandler(403)
def error_403_page(error):
    return render_template(
        'error/error.html',
        error_title=403,
        error_1=4,
        error_2=0,
        error_3=3,
        error_message='资源不可用'
    ), 403


@error_handler.app_errorhandler(401)
def error_401_page(error):
    return render_template(
        'error/error.html',
        error_title=401,
        error_1=4,
        error_2=0,
        error_3=1,
        error_message='没有权限'
    ), 401


@error_handler.app_errorhandler(405)
def error_405_page(error):
    return render_template(
        'error/error.html',
        error_title=405,
        error_1=4,
        error_2=0,
        error_3=5,
        error_message='不被允许的操作'
    ), 405


@error_handler.app_errorhandler(500)
def error_500_page(error):
    return render_template(
        'error/error.html',
        error_title=500,
        error_1=5,
        error_2=0,
        error_3=0,
        error_message='服务器内部错误'
    ), 500
