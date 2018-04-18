# -*- coding: utf-8 -*-
"""
    myflaskblog.main.admin
    ~~~~~~~~~

    管理员功能模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入蓝图模块
from flask import Blueprint

# 导入flask_login模块
from flask_login import login_required, current_user

# 导入必须的模块
from flask import request, url_for, render_template, redirect, abort
from myflaskblog.models import User, Comment, Config
from myflaskblog import db
from myflaskblog.main import _general_method
from myflaskblog.redis_manage import add_redis_user_data, get_redis_user_value
from myflaskblog.main import _form
from flask import current_app, flash


admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def admin_index_page():
    if current_user.is_admin == 1:
        return render_template('/admin/admin.html')
    else:
        abort(403)


@admin.route('/user_manage')
@login_required
def user_manage_page():
    if current_user.is_admin == 1:
        all_user = User.query.filter(User.is_admin != 1)
        page = request.args.get('page', 1, type=int)
        pagination = all_user.paginate(page, per_page=10, error_out=True)
        users = pagination.items
        need_pagination = _general_method.page_mode(
            len(all_user.all()),
            len(users),
            request.args.get('page')
        )
        pagination_url = 'admin.user_manage_page'
        return render_template(
            "/admin/user_manage.html",
            items=users,
            pagination=pagination,
            need_pagination=need_pagination,
            pagination_url=pagination_url
        )
    else:
        abort(403)


@admin.route('/search_user', methods=['GET', 'POST'])
@login_required
def search_user_page():
    if current_user.is_admin == 1:
        if request.method == 'POST' and request.form.get('name'):
            search_name = request.form.get('name')
            add_redis_user_data(current_user.id, 'admin.search_user_page', search_name)
            return _general_method.search(
                'User',
                search_name,
                'admin.search_user_page',
                "/admin/user_manage.html",
                request.args.get('page', 1, type=int),
                None
            )
        elif request.method == 'GET' and request.args.get('page'):
            search_name = get_redis_user_value(current_user.id, 'admin.search_user_page')
            return _general_method.search(
                'User',
                search_name,
                'admin.search_user_page',
                "/admin/user_manage.html",
                request.args.get('page', 1, type=int),
                request.args.get('page')
            )
        else:
            return redirect(url_for('admin.user_manage_page'))
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
        return render_template('/admin/website_config.html')
    else:
        abort(403)


@admin.route('/manage_comment')
@login_required
def manage_comment_page():
    if current_user.is_admin == 1:
        page = request.args.get('page', 1, type=int)
        all_comment = Comment.query.order_by(Comment.create_datetime.desc())
        pagination = all_comment.paginate(page, per_page=10, error_out=True)
        comments = pagination.items
        need_pagination = _general_method.page_mode(
            len(all_comment.all()),
            len(comments),
            request.args.get('page')
        )
        pagination_url = 'admin.manage_comment_page'
        return render_template(
            '/admin/manage_comment.html',
            items=comments,
            pagination=pagination,
            need_pagination=need_pagination,
            pagination_url=pagination_url
        )
    else:
        abort(403)


@admin.route('/search_comment', methods=['GET', 'POST'])
@login_required
def search_comment_page():
    if current_user.is_admin == 1:
        if request.method == 'POST' and request.form.get('name'):
            search_name = request.form.get('name')
            add_redis_user_data(current_user.id, 'admin.search_comment_page', search_name)
            return _general_method.search(
                'Comment',
                search_name,
                'admin.search_comment_page',
                "/admin/manage_comment.html",
                request.args.get('page', 1, type=int),
                None
            )
        elif request.method == 'GET' and request.args.get('page'):
            search_name = get_redis_user_value(current_user.id, 'admin.search_comment_page')
            return _general_method.search(
                'Comment',
                search_name,
                'admin.search_comment_page',
                "/admin/manage_comment.html",
                request.args.get('page', 1, type=int),
                None
            )
        else:
            return redirect(url_for('admin.manage_comment_page'))
    else:
        abort(403)


@admin.route('/website_config', methods=['GET', 'POST'])
@login_required
def website_config():
    if current_user.is_admin == 1:
        config_form = _form.WebsiteConfigFrom()
        profile_photo_form = _form.WebsiteProfilePhotoFrom()
        db_website_name = Config.query.filter_by(item='WEBSITE_NAME').first().value
        db_website_license = Config.query.filter_by(item='WEBSITE_LICENSE').first().value
        if config_form.validate_on_submit():
            website_name = config_form.website_name.data
            website_license = config_form.website_license.data
            Config.query.filter_by(item='WEBSITE_NAME').first().value = website_name
            Config.query.filter_by(item='WEBSITE_LICENSE').first().value = website_license
            db.session.commit()
            flash('修改成功,重启网站后生效')
            return redirect(url_for('admin.website_config'))
        else:
            return render_template(
                '/admin/website_config.html',
                config_form=config_form,
                profile_photo_form=profile_photo_form,
                website_name=db_website_name,
                website_license=db_website_license
            )
    else:
        abort(403)
