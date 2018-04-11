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
from flask_login import login_user, login_required, logout_user, current_user

# 导入必须的模块
from flask import request, flash, url_for, render_template, redirect, abort
from myflaskblog.models import User, Comment
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
        if len(all_user.all()) > 10:
            if len(users) < 10:
                need_pagination = 1
            elif request.args.get('page') and int(request.args.get('page')) * 10 == len(all_user.all()):
                need_pagination = 1
            else:
                need_pagination = 2
        else:
            need_pagination = 0
        return render_template("/admin/user_manage.html", users=users, pagination=pagination, need_pagination=need_pagination)
    else:
        abort(403)


@admin.route('/search_user', methods=['POST'])
@login_required
def search_user_page():
    if current_user.is_admin == 1:
        if request.method == 'POST' and request.form.get('name'):
            search_name = request.form.get('name')
            search_user = User.query.filter(User.is_admin != 1, User.username.ilike('%'+search_name+'%'))
            page = request.args.get('page', 1, type=int)
            pagination = search_user.paginate(page, per_page=10, error_out=True)
            users = pagination.items
            if len(search_user.all()) > 10:
                if len(users) < 10:
                    need_pagination = 1
                elif request.args.get('page') and int(request.args.get('page')) * 10 == len(search_user.all()):
                    need_pagination = 1
                else:
                    need_pagination = 2
            else:
                need_pagination = 0
            return render_template("/admin/user_manage.html", users=users, pagination=pagination, need_pagination=need_pagination)
        else:
            return redirect(url_for('admin.user_manage_page'))
    else:
        abort(403)
    # TODO:换页问题，redis储存上次搜索


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


@admin.route('/manage_comment')
@login_required
def manage_comment_page():
    if current_user.is_admin == 1:
        page = request.args.get('page', 1, type=int)
        all_comment = Comment.query.order_by(Comment.create_datetime.desc())
        pagination = all_comment.paginate(page, per_page=10, error_out=True)
        comments = pagination.items
        if len(all_comment.all()) > 10:
            if len(comments) < 10:
                need_pagination = 1
            elif request.args.get('page') and int(request.args.get('page')) * 10 == len(all_comment.all()):
                need_pagination = 1
            else:
                need_pagination = 2
        else:
            need_pagination = 0
        return render_template('/admin/manage_comment.html', comments=comments, pagination=pagination, need_pagination=need_pagination)
    else:
        abort(403)


@admin.route('/search_comment', methods=['POST'])
@login_required
def search_comment_page():
    if current_user.is_admin == 1:
        if request.method == 'POST' and request.form.get('name'):
            search_name = request.form.get('name')
            search_comment = Comment.query.filter(Comment.title.ilike('%'+search_name+'%'))
            page = request.args.get('page', 1, type=int)
            pagination = search_comment.paginate(page, per_page=10, error_out=True)
            comments = pagination.items
            if len(search_comment.all()) > 10:
                if len(comments) < 10:
                    need_pagination = 1
                elif request.args.get('page') and int(request.args.get('page')) * 10 == len(search_comment.all()):
                    need_pagination = 1
                else:
                    need_pagination = 2
            else:
                need_pagination = 0
            return render_template('/admin/manage_comment.html', comments=comments, pagination=pagination, need_pagination=need_pagination)
        else:
            return redirect(url_for('admin.manage_comment_page'))
    else:
        abort(403)
    # TODO:换页问题，redis储存上次搜索
