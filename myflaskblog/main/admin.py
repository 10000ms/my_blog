#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
管理页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user

# 导入必须的模块
from flask import request, flash, url_for, render_template, redirect
from myflaskblog.models import User

admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def admin_index_page():
    return render_template('/user/admin.html')