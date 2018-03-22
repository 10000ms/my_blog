#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
用户页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

# 导入必须的模块
from flask import request, flash, url_for, render_template, redirect, abort
from myflaskblog.models import User, Comment
from myflaskblog import db
import hashlib

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user

# 导入WTF模块
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login_page():
    form = UserloginForm()
    if form.validate_on_submit():
        account = form.account.data
        check_login_user = User.query.filter_by(account=account).first()
        if not check_login_user:
            flash('该用户不存在')
            return redirect(url_for('user.login_page'))
        elif not check_login_user.verify_password(form.password.data):
            flash('密码错误')
            return redirect(url_for('user.login_page'))
        else:
            login_user(check_login_user, remember=True)
            return redirect(url_for('user.login_user_page'))
    else:
        return render_template('/user/login.html', form=form)
    # TODO：优化错误显示，ajax闪现返回


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
    form = UserregisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(account=form.account.data).first():
            flash('用户已存在')
            return redirect(url_for('user.register_page'))
        else:
            account = form.account.data
            password = form.password.data
            username = form.username.data
            email = form.email.data
            new_user = User(account, password, username, email)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('user.login_user_page'))
    else:
        return render_template('/user/register.html', form=form)


@user.route('/person_setting', methods=['GET', 'POST'])
@login_required
def person_setting_page():
    form = UsernameForm()
    if form.validate_on_submit():
        rename_user = User.query.filter_by(id=current_user.id).first()
        rename_user.username = form.username.data
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('user.person_setting_page'))
    else:
        page = request.args.get('page', 1, type=int)
        user_comment = Comment.query.filter_by(user_id=current_user.id)
        pagination = user_comment.paginate(page, per_page=10, error_out=True)
        comments = pagination.items
        return render_template('/user/person_setting.html', form=form, comments=comments, pagination=pagination)


class UserloginForm(FlaskForm):
    account = StringField('帐号', [DataRequired('帐号必填！'), Length(min=6, max=20, message='账户必须介于6-20字符！')])
    password = PasswordField('密码', [DataRequired('密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    submit = SubmitField('提交')


class UserregisterForm(FlaskForm):
    account = StringField('帐号', [DataRequired('帐号必填！'), Length(min=6, max=20, message='帐号必须介于6-20字符！')])
    password = PasswordField('密码', [DataRequired('密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    confirm = PasswordField('重复密码', [DataRequired('重复密码必填！'), EqualTo('password', message='两次密码输入不一致！')])
    username = StringField('用户名', [DataRequired('重复密码必填！'), Length(min=6, max=20, message='用户名必须介于6-20字符！')])
    email = StringField('email', [DataRequired('email必填！'), Length(min=3, max=20, message='email必须介于3-20字符！')])
    submit = SubmitField('提交')


class UsernameForm(FlaskForm):
    username = StringField('用户名', [DataRequired('重复密码必填！'), Length(min=6, max=20, message='用户名必须介于6-20字符！')])
    submit = SubmitField('提交')
