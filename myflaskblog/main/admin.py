# -*- coding: utf-8 -*-
"""
    myflaskblog.main.admin
    ~~~~~~~~~

    管理员功能模块
    内含可以直接访问的页面7个，涵盖从主页到用户，评论以及网站设置功能

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入flask内的相关类
from flask import Blueprint
from flask import flash
from flask import url_for
from flask import render_template
from flask import redirect
from flask import abort
from flask import request
# 导入flask_login模块内检验登陆和获取当前用户类
from flask_login import login_required
from flask_login import current_user

# 导入项目中相关功能
from myflaskblog import db
from myflaskblog.models import User
from myflaskblog.models import Comment
from myflaskblog.models import Config
from myflaskblog.main import _general_method
from myflaskblog.main import _form
from myflaskblog.redis_manage import add_redis_user_data
from myflaskblog.redis_manage import get_redis_user_value


admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def admin_index_page():
    """
    管理界面主页，判断用户权限直接后直接渲染html

    :return: 渲染/admin/admin.html
    """
    if current_user.is_admin == 1:
        return render_template('/admin/admin.html')
    else:
        abort(403)


@admin.route('/user_manage')
@login_required
def user_manage_page():
    """
    用户管理页面，判断用户权限后获取数据库非管理员用户，使用page_mode判断需要页码模块后渲染输出

    :return: 渲染/admin/user_manage.html
    """
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
        # 搜索功能可能存在换页到不同的模块，所以需要指定url
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
    """
    管理功能下的用户搜索页面，先判断用户权限，然后判断方法。
    POST为初次传递搜索关键字，根据关键字查询结果，并将结果存入redis中，方便分页使用
    GET为搜索结果的第二页及之后，提出redis中的关键字，再次进行搜索，输出第二页

    :return: 使用搜索结果的用户渲染/admin/user_manage.html
    """
    if current_user.is_admin == 1:
        if request.method == 'POST' and request.form.get('name'):
            search_name = request.form.get('name')
            # 搜索关键字存入redis
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
            # 提取搜索关键字，再次进行搜索
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
    """
    删除用户页面，无法直接打开，前端js将需要删除的用户id传输过来

    :param user_id: 需要删除的用户id
    :return: ajax功能，返回信息让前端js获知成功即可
    """
    if current_user.is_admin == 1:
        delete_user = User.query.filter_by(id=user_id).first()
        db.session.delete(delete_user)
        db.session.commit()
        return '删除成功'
    else:
        abort(403)
# TODO：完善有评论或文章的用户无法删除


@admin.route('/blog_setting')
@login_required
def blog_setting_page():
    """
    网站设置主页，判断用户权限直接后直接渲染html

    :return: 渲染/admin/website_config.html
    """
    if current_user.is_admin == 1:
        return render_template('/admin/website_config.html')
    else:
        abort(403)


@admin.route('/manage_comment')
@login_required
def manage_comment_page():
    """
    评论管理页面，判断用户权限后获取数据库非管理员用户，使用page_mode判断需要页码模块后渲染输出

    :return: 渲染/admin/manage_comment.html
    """
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
        # 搜索功能可能存在换页到不同的模块，所以需要指定url
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
    """
    管理功能下的评论搜索页面，先判断用户权限，然后判断方法。
    POST为初次传递搜索关键字，根据关键字查询结果，并将结果存入redis中，方便分页使用
    GET为搜索结果的第二页及之后，提出redis中的关键字，再次进行搜索，输出第二页

    :return: 使用搜索结果的评论渲染/admin/manage_comment.html
    """
    if current_user.is_admin == 1:
        if request.method == 'POST' and request.form.get('name'):
            search_name = request.form.get('name')
            # 搜索关键字存入redis
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
            # 提取搜索关键字，再次进行搜索
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
    """
     网站设置的设置页面
     GET为初次访问，获取数据库中设置信息输出渲染模板
     POST为传输更新form的数据，判断填入数据库后跳转GET页面

    :return: 渲染/admin/website_config.html
              POST成功会额外附带flash信息
    """
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
