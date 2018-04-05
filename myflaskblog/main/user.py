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
from myflaskblog.email_sender import send_email
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from myflaskblog.main import _form

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user


user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login_page():
    form = _form.UserLoginForm()
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
    form = _form.UserRegisterForm()
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
            token = new_user.generate_token('confirm')
            send_email(new_user.email, '请确认您的帐号', 'email/confirm', user=new_user, token=token)
            login_user(new_user, remember=True)
            return redirect(url_for('user.login_user_page'))
    else:
        return render_template('/user/register.html', form=form)


@user.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('index.index_page'))
    elif current_user.check_token(token, 'confirm'):
        return '激活成功'
    else:
        return '邮箱激活失败，请重试'
    # TODO:未登陆用户同样可以激活，使用正确跳转


@user.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and str(request.endpoint)[:5] != 'user.'\
            and request.endpoint != 'static':
        return redirect(url_for('user.unconfirmed'))


@user.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('index.index_page'))
    return render_template('/user/unconfirmed.html')
    # TODO:增加是否需要修改邮箱


@user.route('/send_email_again')
@login_required
def send_email_again():
    token = current_user.generate_token('confirm')
    send_email(current_user.email, '请确认您的帐号', 'email/confirm', user=current_user, token=token)
    flash('已重发验证邮件')
    return redirect(url_for('user.unconfirmed'))
    # TODO:检测重发间隔


@user.route('/reset_email', methods=['GET', 'POST'])
@login_required
def reset_email():
    form = _form.ResetEmailForm()
    if form.validate_on_submit():
        if form.email.data == current_user.email:
            flash('新邮箱与旧邮箱重复')
            return redirect(url_for('user.reset_email'))
        reset_email_user = User.query.filter_by(id=current_user.id).first()
        reset_email_user.email = form.email.data
        reset_email_user.confirmed = False
        db.session.commit()
        token = current_user.generate_token('confirm')
        send_email(current_user.email, '请确认您的新邮箱', 'email/resetemail', user=current_user, token=token)
        flash('提交成功，请留意新邮箱的信息')
        return redirect(url_for('user.reset_email'))
    else:
        return render_template('/user/reset_email.html', form=form)


@user.route('/forget_password', methods=['GET', 'POST'])
def forget_password():
    form = _form.ForgetPasswordForm()
    if current_user.is_authenticated:
        flash('已登陆用户请勿进行此操作')
        return redirect(url_for('index.index_page'))
    elif form.validate_on_submit():
        if not User.query.filter_by(account=form.account.data).first():
            flash('未找到该用户')
            return redirect(url_for('user.forget_password'))
        need_resetpassword_user = User.query.filter_by(account=form.account.data).first()
        if need_resetpassword_user.email != form.email.data:
            flash('用户email错误')
            return redirect(url_for('user.forget_password'))
        token = need_resetpassword_user.generate_token('resetpassword')
        send_email(need_resetpassword_user.email, '请重置您的密码', 'email/resetpassword', user=need_resetpassword_user, token=token)
        flash('重置密码邮件已发送，请登陆邮箱根据提示进行密码修改')
        return redirect(url_for('user.forget_password'))
    else:
        return render_template('/user/forget_password.html', form=form)
    # TODO:注册未激活用户忘记密码


@user.route('/forget_password_setting/<token>', methods=['GET', 'POST'])
def forget_password_setting(token):
    form = _form.ResetForgetPasswordForm()
    form.reset_password_token.data = token
    return render_template('/user/forget_password_setting.html', form=form)
    # TODO:忘记密码部分更加合理


@user.route('/forget_password_setting_password', methods=['POST'])
def forget_password_setting_password():
    form = _form.ResetForgetPasswordForm()
    if form.validate_on_submit():
        ss = Serializer(current_app.config['SECRET_KEY'])
        try:
            get_data = ss.loads(form.reset_password_token.data)
        except:
            return '出错了'
        user_id = get_data.get('rp')
        forget_password_user = User.query.filter_by(id=user_id).first()
        forget_password_user.change_password(form.password.data)
        flash('密码修改成功')
        return render_template('/user/forget_password_setting.html', form=form)
    else:
        abort(404)


@user.route('/reset_password', methods=['GET', 'POST'])
@login_required
def reset_password():
    form = _form.ResetPasswordForm()
    if form.validate_on_submit():
        if not current_user.verify_password(form.old_password.data):
            flash('密码错误')
            return redirect(url_for('user.reset_password'))
        if form.old_password.data == form.password.data:
            flash('新旧密码重复')
            return redirect(url_for('user.reset_password'))
        reset_password_user = User.query.filter_by(id=current_user.id).first()
        reset_password_user.change_password(form.password.data)
        flash('密码修改成功')
        return redirect(url_for('user.reset_password'))
    else:
        return render_template('/user/reset_password.html', form=form)


@user.route('/person_setting', methods=['GET', 'POST'])
@login_required
def person_setting_page():
    form = _form.UsernameForm()
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


@user.route('/set_profile_photo')
@login_required
def set_profile_photo():
    form = _form.ProfilePhotoForm()
    return render_template('/user/set_profile_photo.html', form=form)
