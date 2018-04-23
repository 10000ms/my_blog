# -*- coding: utf-8 -*-
"""
    myflaskblog.main.user
    ~~~~~~~~~

    用户管理模块
    内涵可以直接访问的页面7个，覆盖用户注册登陆使用及权限管理部分功能。

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入uuid创建唯一id
import uuid
# 导入Serializer加密
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 导入flask内的相关类
from flask import Blueprint
from flask import request
from flask import flash
from flask import url_for
from flask import render_template
from flask import redirect
from flask import abort
from flask import current_app
from flask import make_response
# 导入flask_login模块内登入登出检验登陆和获取当前用户类
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user

# 导入项目中相关功能
from myflaskblog import db
from myflaskblog.main import _form
from myflaskblog.main import _general_method
from myflaskblog.models import User
from myflaskblog.models import Comment
from myflaskblog.email_sender import send_email
from myflaskblog.img_manage import get_profile_photo_folder
from myflaskblog.redis_manage import user_login_out
from myflaskblog.redis_manage import user_session_check
from myflaskblog.redis_manage import check_send_time
from myflaskblog.redis_manage import email_token_check
from myflaskblog.redis_manage import email_token_set


user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login_page():
    """
    用户登陆界面与接受登陆信息进行用户登陆
    user_session用户确保用户单点登陆

    :return:GET: 渲染/user/login.html
             POST: 判断登陆跳转
    """
    form = _form.UserLoginForm()
    if form.validate_on_submit():
        account = form.account.data
        check_login_user = User.query.filter_by(account=account).first()
        # 帐号确认
        if not check_login_user:
            flash('该用户不存在')
            return redirect(url_for('user.login_page'))
        # 密码确认
        if not check_login_user.verify_password(form.password.data):
            flash('密码错误')
            return redirect(url_for('user.login_page'))
        user_session = str(uuid.uuid1())
        # 单点登陆确认
        if not user_session_check(check_login_user.id, user_session):
            flash('该用户已登陆，请稍后再试')
            return redirect(url_for('user.login_page'))
        login_user(check_login_user, remember=True)
        response = make_response(redirect(url_for('user.login_user_page')))
        response.set_cookie("user_session", user_session)
        return response
    else:
        return render_template('/user/login.html', form=form)


@user.route('/user_page')
@login_required
def login_user_page():
    """
    判断登陆用户权限等级，跳转不同页面

    :return: 管理员：跳转admin.admin_index_page
              普通用户：渲染/user/user.html
    """
    now_login_user = current_user
    if now_login_user.is_admin == 1:
        return redirect(url_for('admin.admin_index_page'))
    elif now_login_user.is_admin == 0:
        return render_template('/user/user.html')


@user.route('/logout')
@login_required
def logout():
    """
    用户登出，先清除保存的临时信息后登出

    :return: 首页
    """
    # 清除redis中相关信息
    user_login_out(current_user.id)
    logout_user()  # 登出用户
    return redirect(url_for('index.index_page'))


@user.route('/register', methods=['GET', 'POST'])
def register_page():
    """
    用户注册界面与接受登陆信息进行用户注册
    注册成功后会发邮件让用户进行认证

    :return:GET: 渲染/user/register.html
             POST: 验证注册后跳转user.login_user_page
    """
    form = _form.UserRegisterForm()
    if form.validate_on_submit():
        # 检测帐号
        if User.query.filter_by(account=form.account.data).first():
            flash('用户已存在')
            return redirect(url_for('user.register_page'))
        # 检测email
        if User.query.filter_by(email=form.email.data).first():
            flash('email已注册')
            return redirect(url_for('user.register_page'))
        account = form.account.data
        password = form.password.data
        username = form.username.data
        email = form.email.data
        new_user = User(account, password, username, email)
        db.session.add(new_user)
        db.session.commit()
        token = new_user.generate_token('confirm')
        # 发送验证邮件
        send_email(new_user.email, '请确认您的帐号', 'email/confirm', user=new_user, token=token)
        login_user(new_user, remember=True)
        return redirect(url_for('user.login_user_page'))
    else:
        return render_template('/user/register.html', form=form)


@user.route('/confirm/<token>')
def confirm(token):
    """
    邮箱激活认证，注册和更换邮箱时使用

    :param token: 确认信息用token
    :return: 激活成功跳转user.person_setting_page
    """
    if current_user.is_authenticated and current_user.confirmed:
        return redirect(url_for('index.index_page'))
    else:
        # 判断邮箱是否为最新邮箱
        if not email_token_check(token):
            flash('请使用最新设置邮箱激活')
            return redirect(url_for('user.login_page'))
        confirm_user = _general_method.check_token(token)
        # 判断用户是否认证
        if confirm_user:
            # 未登陆认证直接登陆
            if not current_user.is_authenticated:
                login_user(User.query.filter_by(id=confirm_user).first(), remember=True)
            flash('激活成功')
            return redirect(url_for('user.person_setting_page'))
        else:
            flash('已激活用户，请登陆')
            return redirect(url_for('user.login_page'))


@user.before_app_request
def before_request():
    """
    request前检测，只检验登陆用户。
    检测内容：
    1.单点登陆
    2.用户是否经过邮箱认证

    :return: 通过检验不影响正常使用
    """
    # 单点登陆检验1
    if request.cookies.get('user_session') \
            and current_user.is_authenticated \
            and not user_session_check(current_user.id, request.cookies.get('user_session')):
            logout_user()
            flash('该用户已登陆')
            return redirect(url_for('user.login_page'))
    # 单点登陆检验2
    if current_user.is_authenticated and not request.cookies.get('user_session'):
        logout_user()
        flash('登陆已失效，请重新登陆')
        return redirect(url_for('user.login_page'))
    # 用户认证检验
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and str(request.endpoint)[:5] != 'user.'\
            and request.endpoint != 'static':
        return redirect(url_for('user.unconfirmed'))


@user.route('/unconfirmed')
@login_required
def unconfirmed():
    """
    未认证用户界面

    :return: 渲染/user/unconfirmed.html
    """
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('index.index_page'))
    return render_template('/user/unconfirmed.html')


@user.route('/send_email_again')
@login_required
def send_email_again():
    """
    验证邮件重新发送，会检测发送间隔

    :return: 带相应flash信息跳转user.unconfirmed
    """
    token = current_user.generate_token('confirm')
    # 发送间隔检验
    if check_send_time(current_user.id):
        send_email(current_user.email, '请确认您的帐号', 'email/confirm', user=current_user, token=token)
        flash('已重发验证邮件')
    else:
        flash('请勿频繁操作')
    return redirect(url_for('user.unconfirmed'))


@user.route('/reset_email', methods=['GET', 'POST'])
@login_required
def reset_email():
    """
    重设认证邮箱页面和接受新认证邮箱

    :return:GET: 渲染/user/reset_email.html
             POST: 验证重发后跳转user.reset_email
    """
    form = _form.ResetEmailForm()
    if form.validate_on_submit():
        # 新旧邮箱检验
        if form.email.data == current_user.email:
            flash('新邮箱与旧邮箱重复')
            return redirect(url_for('user.reset_email'))
        # 邮箱与其他邮箱检验
        if User.query.filter_by(email=form.email.data).first():
            flash('email已存在')
            return redirect(url_for('user.reset_email'))
        # 邮件间隔检验
        if check_send_time(current_user.id):
            reset_email_user = User.query.filter_by(id=current_user.id).first()
            reset_email_user.email = form.email.data
            reset_email_user.confirmed = False
            db.session.commit()
            token = current_user.generate_token('confirm')
            email_token_set(current_user.id, token)
            send_email(current_user.email, '请确认您的新邮箱', 'email/resetemail', user=current_user, token=token)
            flash('提交成功，请留意新邮箱的信息')
        else:
            flash('请勿频繁操作')
        return redirect(url_for('user.reset_email'))
    else:
        return render_template('/user/reset_email.html', form=form)


@user.route('/forget_password', methods=['GET', 'POST'])
def forget_password():
    """
    忘记密码页面，或接受忘记密码用户信息

    :return: GET: 渲染/user/forget_password.html
             POST: 验证发送邮件后跳转user.forget_password
    """
    form = _form.ForgetPasswordForm()
    # 检测用户是否登陆
    if current_user.is_authenticated:
        flash('已登陆用户请勿进行此操作')
        return redirect(url_for('index.index_page'))
    elif form.validate_on_submit():
        # 帐号检测
        if not User.query.filter_by(account=form.account.data).first():
            flash('未找到该用户')
            return redirect(url_for('user.forget_password'))
        need_reset_password_user = User.query.filter_by(account=form.account.data).first()
        # 邮箱检测
        if not need_reset_password_user.confirmed:
            flash('邮箱未激活用户无法使用该功能')
            return redirect(url_for('user.forget_password'))
        if need_reset_password_user.email != form.email.data:
            flash('用户email错误')
            return redirect(url_for('user.forget_password'))
        # 发送间隔检测
        if check_send_time(need_reset_password_user):
            token = need_reset_password_user.generate_token('resetpassword')
            send_email(
                need_reset_password_user.email,
                '请重置您的密码',
                'email/resetpassword',
                user=need_reset_password_user,
                token=token
            )
            flash('重置密码邮件已发送，请登陆邮箱根据提示进行密码修改')
        else:
            flash('请勿频繁操作')
        return redirect(url_for('user.forget_password'))
    else:
        return render_template('/user/forget_password.html', form=form)


@user.route('/forget_password_setting/<token>')
def forget_password_setting(token):
    """
    重设忘记密码界面，邮箱忘记密码重设跳转地址

    :param token: 确认信息用token
    :return: 渲染/user/forget_password_setting.html
    """
    form = _form.ResetForgetPasswordForm()
    form.reset_password_token.data = token
    return render_template('/user/forget_password_setting.html', form=form)


@user.route('/forget_password_setting_password', methods=['POST'])
def forget_password_setting_password():
    """
    重设用户密码

    :return:带flash信息的跳转user.login_page
    """
    form = _form.ResetForgetPasswordForm()
    if form.validate_on_submit():
        ss = Serializer(current_app.config['SECRET_KEY'])
        try:
            get_data = ss.loads(form.reset_password_token.data)
        except:
            flash('出错了')
            return redirect(url_for('user.login_page'))
        user_id = get_data.get('rp')
        forget_password_user = User.query.filter_by(id=user_id).first()
        if not forget_password_user:
            flash('出错了')
            return redirect(url_for('user.login_page'))
        forget_password_user.change_password(form.password.data)
        flash('密码修改成功，请用新密码登陆')
        return redirect(url_for('user.login_page'))
    else:
        abort(404)


@user.route('/reset_password', methods=['GET', 'POST'])
@login_required
def reset_password():
    """
    重设密码，或接收重设信息

    :return:GET: 渲染/user/forget_password.html
             POST: 验证发送邮件后跳转user.forget_password
    """
    form = _form.ResetPasswordForm()
    if form.validate_on_submit():
        # 验证旧密码
        if not current_user.verify_password(form.old_password.data):
            flash('密码错误')
            return redirect(url_for('user.reset_password'))
        # 新旧密码确认
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
    """
    用户个人设置页面，可以设置头像，修改验证邮箱，修改密码
    或者直接进行用户名修改和评论管理

    POST是接收修改后的用户名

    :return: 渲染/user/person_setting.html
    """
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
    """
    用户头像设置页面
    （上传头像为ajax方法，由另外页面接收）

    :return: 渲染/user/set_profile_photo.html
    """
    if current_user.confirmed:
        form = _form.ProfilePhotoForm()
        folder = get_profile_photo_folder()
        return render_template('/user/set_profile_photo.html', form=form, folder=folder)
    else:
        return redirect(url_for('index.index_page'))
