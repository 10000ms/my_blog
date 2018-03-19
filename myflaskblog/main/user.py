#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
用户页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

# 导入必须的模块
from flask import request, flash, url_for, render_template, redirect
from myflaskblog.models import User
from myflaskblog import db
import hashlib

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user

# 导入WTF模块
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login_page():
    form = UserloginForm(request.form)
    if form.validate_on_submit():
        account = request.form.get('account')
        check_login_user = User.query.filter_by(account=account).first()
        if not check_login_user:
            # flash('该用户不存在')
            return '该用户不存在'
        elif not check_login_user.verify_password(request.form.get('password')):
            #  flash('密码错误')
            return '密码错误'
        else:
            login_user(check_login_user, remember=True)
            return redirect(url_for('user.login_user_page'))
    else:
        return render_template('/user/login.html', form=form)
    # TODO：优化错误显示


@user.route('/user_page')
@login_required
def login_user_page():
    now_login_user = current_user
    if now_login_user.is_admin == 1:
        return redirect(url_for('admin.admin_index_page'))
    elif now_login_user.is_admin == 0:
        return render_template('/user/user.html')


@user.route('/logout')
@login_required
def logout():
    logout_user()  # 登出用户
    return redirect(url_for('index.index_page'))


@user.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password != confirm:
            return '两次输入密码不一致'
        elif User.query.filter_by(account=request.form.get('account')).first():
            return '用户已存在'
        else:
            account = request.form.get('account')
            username = request.form.get('username')
            email = request.form.get('email')
            new_user = User(account, password, username, email)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('user.login_user_page'))
    else:
        form = UserregisterForm(request.form)
        return render_template('/user/register.html', form=form)


class UserloginForm(FlaskForm):
    account = StringField('帐号', [DataRequired('帐号必填！'), Length(min=6, max=20, message='账户必须介于6-20字符！')])
    password = PasswordField('密码', [DataRequired('密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    confirm = PasswordField('重复密码', [DataRequired('重复密码必填！'), EqualTo('password', message='两次密码输入不一致！')])


class UserregisterForm(FlaskForm):
    account = StringField('帐号', [DataRequired('帐号必填！'), Length(min=6, max=20, message='帐号必须介于6-20字符！')])
    password = PasswordField('密码', [DataRequired('密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    confirm = PasswordField('重复密码', [DataRequired('重复密码必填！'), EqualTo('password', message='两次密码输入不一致！')])
    username = StringField('用户名', [DataRequired('重复密码必填！'), Length(min=6, max=20, message='用户名必须介于6-20字符！')])
    email = StringField('email', [DataRequired('email必填！'), Length(min=3, max=20, message='email必须介于3-20字符！')])
