#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
出错页面模块
'''

# 导入项目模块
# from myflaskblog import app
from flask import Blueprint

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
    return '404 Not Found', 404


@error_handler.app_errorhandler(403)
def error_403_page(error):
    return '403 Forbidden', 403


@error_handler.app_errorhandler(410)
def error_410_page(error):
    return '410 Gone', 410


@error_handler.app_errorhandler(500)
def error_500_page(error):
    return '500 Internal Server Error', 500
