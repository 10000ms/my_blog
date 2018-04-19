# -*- coding: utf-8 -*-
"""
    myflaskblog.main._form
    ~~~~~~~~~

    wtf表格模块
    内含需要用到的表格共12个

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入WTF模块
from flask_wtf import FlaskForm
# 导入所需要的Field
from wtforms import StringField
from wtforms import SubmitField
from wtforms import HiddenField
from wtforms import PasswordField
from wtforms import FileField
# 导入验证模块
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import Regexp


class ArticleForm(FlaskForm):
    title = StringField('标题', [
        DataRequired('标题必填！'),
        Length(min=1, max=100, message='标题必须介于1-100字符！')
    ])
    keyword = StringField('关键词', [
        DataRequired('关键词必填！'),
        Length(min=1, max=100, message='关键词必须介于1-100字符！')
    ])
    description = StringField('描述', [
        DataRequired('描述必填！'),
        Length(min=1, max=1000, message='描述必须介于1-1000字符！')
    ])


class CommentForm(FlaskForm):
    title = StringField('标题', [
        DataRequired('标题必填！'),
        Length(min=1, max=100, message='标题必须介于1-100字符！')
    ])


class UserLoginForm(FlaskForm):
    account = StringField('帐号：', [
        DataRequired('帐号必填！'),
        Length(min=6, max=20, message='账户必须介于6-20字符！'),
        Regexp(r'\w+', message='账户必须是字母数字或者_')
    ], render_kw={"placeholder": "请输入帐号"})
    password = PasswordField('密码：', [
        DataRequired('密码必填！'),
        Length(min=6, max=20, message='密码必须介于6-20字符！'),
        Regexp(r'(?!^\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$).{6,20}', message='密码错误')
    ], render_kw={"placeholder": "请输入密码"})
    submit = SubmitField('提交')


class UserRegisterForm(FlaskForm):
    account = StringField('帐号', [
        DataRequired('帐号必填！'),
        Length(min=6, max=20, message='帐号必须介于6-20字符！'),
        Regexp(r'\w+', message='账户必须是字母数字或者_')
    ], render_kw={"placeholder": "6-20字符的帐号"})
    password = PasswordField('密码', [
        DataRequired('密码必填！'),
        Length(min=6, max=20, message='密码必须介于6-20字符！'),
        Regexp(
            r'(?!^\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$).{6,}',
            message='密码必须由字母、数字或符号2种或以上的字符类型组成'
        )
    ], render_kw={"placeholder": "6-20字符并且含义字母、数字或符号中的2种"})
    confirm = PasswordField('重复密码', [
        DataRequired('重复密码必填！'),
        EqualTo('password', message='两次密码输入不一致！')
    ], render_kw={"placeholder": "再次输入密码"})
    username = StringField('用户名', [
        DataRequired('用户名必填！'),
        Length(min=2, max=20, message='用户名必须介于2-20字符！')
    ], render_kw={"placeholder": "2-20字符用户名"})
    email = StringField('email', [
        DataRequired('email必填！'),
        Length(min=3, max=40, message='email必须介于3-40字符！'),
        Regexp(r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$', message='邮箱格式不对')
    ], render_kw={"placeholder": "您常用的email地址"})
    submit = SubmitField('提交')


class UsernameForm(FlaskForm):
    username = StringField('用户名修改', [
        DataRequired('用户名必填！'),
        Length(min=2, max=20, message='用户名必须介于2-20字符！')
    ], render_kw={"placeholder": "您新的用户名"})
    submit = SubmitField('提交')


class ResetEmailForm(FlaskForm):
    email = StringField('email', [
        DataRequired('email必填！'),
        Length(min=3, max=20, message='email必须介于3-20字符！'),
        Regexp(r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$', message='邮箱格式不对')
    ], render_kw={"placeholder": "您常用的email地址"})
    submit = SubmitField('提交')


class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', [
        DataRequired('旧密码必填！'),
        Length(min=6, max=20, message='密码必须介于6-20字符！'),
        Regexp(
            r'(?!^\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$).{6,}',
            message='密码必须由字母、数字或符号2种或以上的字符类型组成'
        )
    ], render_kw={"placeholder": "您现在的密码"})
    password = PasswordField('新密码', [
        DataRequired('新密码必填！'),
        Length(min=6, max=20, message='密码必须介于6-20字符！'),
        Regexp(r'(?!^\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$).{6,}', message='邮箱格式不对')
    ], render_kw={"placeholder": "您要设置的新密码"})
    confirm = PasswordField('重复密码', [
        DataRequired('重复密码必填！'),
        EqualTo('password', message='两次密码输入不一致！')
    ], render_kw={"placeholder": "重复新密码"})
    submit = SubmitField('提交')


class ForgetPasswordForm(FlaskForm):
    account = StringField('帐号', [
        DataRequired('帐号必填！'),
        Length(min=6, max=20, message='帐号必须介于6-20字符！'),
        Regexp(r'\w+', message='账户必须是字母数字或者_')
    ], render_kw={"placeholder": "请输入帐号"})
    email = StringField('email', [
        DataRequired('email必填！'),
        Length(min=3, max=20, message='email必须介于3-20字符！'),
        Regexp(r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$', message='邮箱格式不对')
    ], render_kw={"placeholder": "请输入该帐号的email地址"})
    submit = SubmitField('提交')


class ResetForgetPasswordForm(FlaskForm):
    reset_password_token = HiddenField()
    password = PasswordField('新密码', [
        DataRequired('新密码必填！'),
        Length(min=6, max=20, message='密码必须介于6-20字符！'),
        Regexp(
            r'(?!^\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$).{6,}',
            message='密码必须由字母、数字或符号2种或以上的字符类型组成')
    ], render_kw={"placeholder": "6-20字符并且含义字母、数字或符号中的2种"})
    confirm = PasswordField('重复密码', [
        DataRequired('重复密码必填！'),
        EqualTo('password', message='两次密码输入不一致！')
    ], render_kw={"placeholder": "再次输入密码"})
    submit = SubmitField('提交')


class ProfilePhotoForm(FlaskForm):
    profile_photo = FileField('新头像', [DataRequired()])


class WebsiteProfilePhotoFrom(FlaskForm):
    profile_photo = FileField('新网站头像', [DataRequired()])


class WebsiteConfigFrom(FlaskForm):
    website_name = StringField('网站名', [
        DataRequired('网站名必填！'),
        Length(min=2, max=20, message='网站名必须介于2-20字符！'),
    ])
    website_license = StringField('网站备案号', [
        DataRequired('网站备必填！'),
        Length(min=10, max=20, message='网站备必须介于10-20字符！'),
    ])
    submit = SubmitField('提交')
