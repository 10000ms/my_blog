#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
wtf表格模块
'''

# 导入WTF模块
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, EqualTo


class ArticleForm(FlaskForm):
    title = StringField('标题', [DataRequired('标题必填！'), Length(min=6, max=20, message='标题必须介于6-20字符！')])
    keyword = StringField('关键词', [DataRequired('关键词必填！'), Length(min=6, max=20, message='关键词必须介于6-20字符！')])
    description = StringField('描述', [DataRequired('描述必填！'), Length(min=6, max=100, message='描述必须介于6-20字符！')])


class CommentForm(FlaskForm):
    title = StringField('标题', [DataRequired('标题必填！'), Length(min=2, max=20, message='账户必须介于2-20字符！')])
    comment = StringField('评论', [DataRequired('评论必填！')])
    submit = SubmitField('提交')


class UserLoginForm(FlaskForm):
    account = StringField('帐号', [DataRequired('帐号必填！'), Length(min=6, max=20, message='账户必须介于6-20字符！')])
    password = PasswordField('密码', [DataRequired('密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    submit = SubmitField('提交')


class UserRegisterForm(FlaskForm):
    account = StringField('帐号', [DataRequired('帐号必填！'), Length(min=6, max=20, message='帐号必须介于6-20字符！')])
    password = PasswordField('密码', [DataRequired('密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    confirm = PasswordField('重复密码', [DataRequired('重复密码必填！'), EqualTo('password', message='两次密码输入不一致！')])
    username = StringField('用户名', [DataRequired('重复密码必填！'), Length(min=6, max=20, message='用户名必须介于6-20字符！')])
    email = StringField('email', [DataRequired('email必填！'), Length(min=3, max=20, message='email必须介于3-20字符！')])
    submit = SubmitField('提交')


class UsernameForm(FlaskForm):
    username = StringField('用户名', [DataRequired('重复密码必填！'), Length(min=6, max=20, message='用户名必须介于6-20字符！')])
    submit = SubmitField('提交')


class ResetEmailForm(FlaskForm):
    email = StringField('email', [DataRequired('email必填！'), Length(min=3, max=20, message='email必须介于3-20字符！')])
    submit = SubmitField('提交')


class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', [DataRequired('旧密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    password = PasswordField('新密码', [DataRequired('新密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    confirm = PasswordField('重复密码', [DataRequired('重复密码必填！'), EqualTo('password', message='两次密码输入不一致！')])
    submit = SubmitField('提交')


class ForgetPasswordForm(FlaskForm):
    account = StringField('帐号', [DataRequired('帐号必填！'), Length(min=6, max=20, message='帐号必须介于6-20字符！')])
    email = StringField('email', [DataRequired('email必填！'), Length(min=3, max=20, message='email必须介于3-20字符！')])
    submit = SubmitField('提交')


class ResetForgetPasswordForm(FlaskForm):
    reset_password_token = HiddenField()
    password = PasswordField('新密码', [DataRequired('新密码必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    confirm = PasswordField('重复密码', [DataRequired('重复密码必填！'), EqualTo('password', message='两次密码输入不一致！')])
    submit = SubmitField('提交')


class ProfilePhotoForm(FlaskForm):
    profile_photo = FileField('图片', [DataRequired()])