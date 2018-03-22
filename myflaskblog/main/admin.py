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
from flask import request, flash, url_for, render_template, redirect, abort
from myflaskblog.models import User
from myflaskblog import db

admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def admin_index_page():
    return render_template('/admin/admin.html')


@admin.route('/user_manage')
@login_required
def user_manage_page():
    if current_user.is_admin == 1:
        all_user = User.query.filter(User.is_admin != 1)
        page = request.args.get('page', 1, type=int)
        pagination = all_user.paginate(page, per_page=10, error_out=True)
        users = pagination.items
        return render_template("/admin/user_manage.html", users=users, pagination=pagination)
    else:
        abort(403)


@admin.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user_page(user_id):
    if current_user.is_admin == 1:
        delete_user = User.query.filter_by(id=user_id).first()
        db.session.delete(delete_user)
        db.session.commit()
        return '删除成功'
    else:
        abort(403)


@admin.route('/blog_setting')
@login_required
def blog_setting_page():
    if current_user.is_admin == 1:
        return render_template('/admin/blog_setting.html')
    else:
        abort(403)


