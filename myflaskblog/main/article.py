# -*- coding: utf-8 -*-
"""
    myflaskblog.main.article
    ~~~~~~~~~

    博客文章处理模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入flask内的相关类
from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify
from flask import redirect
from flask import abort
# 导入flask_login模块内检验登陆和获取当前用户类
from flask_login import login_required
from flask_login import current_user


# 导入项目中相关功能
from myflaskblog import db
from myflaskblog.models import Article
from myflaskblog.models import Comment
from myflaskblog import img_manage
from myflaskblog.main import _form
from myflaskblog.main import _general_method
from myflaskblog.img_manage import get_profile_photo_folder
from myflaskblog.redis_manage import add_redis_user_data
from myflaskblog.redis_manage import get_redis_user_value


article = Blueprint('article', __name__)


@article.route('/<int:article_id>', methods=['GET', 'POST'])
def article_detail_page(article_id):
    """
    文章具体内容页。
    通过获取的文章id查找文章并输出到模板进行渲染，同时输出的还有该文章的评论
    POST是通过ajax获取文章新评论，并添加到数据库功能

    :param article_id: 文章id
    :return: GET: 渲染/article/article.html
              POST: ajax功能，返回信息让前端js获知成功即可
    """
    get_article = Article.query.filter_by(id=article_id).first()
    form = _form.CommentForm()
    if not get_article:
        return '找不到该文章'
    elif request.method == 'POST':
        title = request.form.get('title')
        comment = request.form.get('comment')
        user_id = current_user.id
        article_id = article_id
        new_comment = Comment(title, comment, user_id, article_id)
        db.session.add(new_comment)
        db.session.commit()
        return '评论成功'
    else:
        page = request.args.get('page', 1, type=int)
        get_comment = Comment.query.filter_by(article_id=article_id)
        pagination = get_comment.order_by(Comment.create_datetime.desc()).paginate(
            page, per_page=5, error_out=True)
        comments = pagination.items
        need_pagination = _general_method.page_mode(
            len(get_comment.all()),
            len(comments),
            request.args.get('page'),
            5
        )
        folder = get_profile_photo_folder()
        return render_template(
            "/article/article.html",
            article=get_article,
            form=form,
            comments=comments,
            pagination=pagination,
            need_pagination=need_pagination,
            folder=folder
        )


@article.route('/new_article', methods=['GET', 'POST'])
@login_required
def new_article_page():
    """
    新文章页面，并可以接受新文章信息写入数据库

    :return:GET: 渲染/article/new_article.html
             POST: ajax功能，返回信息让前端js获知成功即可
    """
    if request.method == 'POST' and current_user.is_admin == 1:
        new_article_title = request.form.get('title')
        if not new_article_title:
            return '出错了'
        new_article_keyword = request.form.get('title')
        new_article_description = request.form.get('description')
        new_article_content = request.form.get('content')
        new_article_user_id = current_user.id
        new_article = Article(
            new_article_title,
            new_article_keyword,
            new_article_description,
            new_article_content,
            new_article_user_id
        )
        db.session.add(new_article)
        db.session.commit()
        img_manage.img_add_article_id(new_article.id, new_article.content)
        return '新文章添加成功'
    elif current_user.is_admin == 1:
        form = _form.ArticleForm()
        return render_template('/article/new_article.html', form=form)
    else:
        abort(403)


@article.route('/manage_article')
@login_required
def manage_article_page():
    """
    文章管理页面，判断用户权限后获取数据库非管理员用户，使用page_mode判断需要页码模块后渲染输出

    :return: 渲染/article/manage_article.html
    """
    if current_user.is_admin == 1:
        page = request.args.get('page', 1, type=int)
        all_articles = Article.query.order_by(Article.create_datetime.desc())
        pagination = all_articles.paginate(page, per_page=10, error_out=True)
        articles = pagination.items
        need_pagination = _general_method.page_mode(
            len(all_articles.all()),
            len(articles),
            request.args.get('page')
        )
        # 搜索功能可能存在换页到不同的模块，所以需要指定url
        pagination_url = 'article.manage_article_page'
        return render_template(
            "/article/manage_article.html",
            items=articles,
            pagination=pagination,
            need_pagination=need_pagination,
            pagination_url=pagination_url
        )
    else:
        abort(403)


@article.route('/search', methods=['GET', 'POST'])
@login_required
def search_article_page():
    """
    文章管理下的文章搜索页面，先判断用户权限，然后判断方法。
    POST为初次传递搜索关键字，根据关键字查询结果，并将结果存入redis中，方便分页使用
    GET为搜索结果的第二页及之后，提出redis中的关键字，再次进行搜索，输出第二页

    :return: 使用搜索结果的文章渲染/article/manage_article.html
    """
    if current_user.is_admin == 1:
        if request.method == 'POST'and request.form.get('name'):
            search_name = request.form.get('name')
            # 搜索关键字存入redis
            add_redis_user_data(current_user.id, 'article.search_article_page', search_name)
            return _general_method.search(
                'Article',
                search_name,
                'article.search_article_page',
                "/article/manage_article.html",
                request.args.get('page', 1, type=int),
                None
            )
        elif request.method == 'GET' and request.args.get('page'):
            # 提取搜索关键字，再次进行搜索
            search_name = get_redis_user_value(current_user.id, 'article.search_article_page')
            return _general_method.search(
                'Article',
                search_name,
                'article.search_article_page',
                "/article/manage_article.html",
                request.args.get('page', 1, type=int),
                request.args.get('page')
            )
        else:
            return redirect(url_for('article.manage_article_page'))
    else:
        abort(403)


@article.route('/change_article/<int:article_id>', methods=['GET', 'POST'])
@login_required
def change_article_page(article_id):
    """
    修改文章页面。
    GET：提取需要修改的文章

    :param article_id: 文章id
    :return:
    """
    if request.method == 'POST' and current_user.is_admin == 1:
        new_article_title = request.form.get('title')
        if not new_article_title:
            return '出错了'
        need_change_article = Article.query.filter_by(id=article_id).first()
        need_change_article.title = request.form.get('title')
        need_change_article.keyword = request.form.get('keyword')
        need_change_article.description = request.form.get('description')
        need_change_article.content = request.form.get('content')
        db.session.commit()
        img_manage.img_change_article_id(article_id, need_change_article.content)
        return url_for('article.article_detail_page', article_id=article_id)
    elif current_user.is_admin == 1:
        need_change_article = Article.query.filter_by(id=article_id).first()
        form = _form.ArticleForm()
        return render_template('/article/change_article.html', article=need_change_article, form=form)
    else:
        abort(403)


@article.route('/delete_article/<int:article_id>', methods=['POST'])
@login_required
def delete_article_page(article_id):
    if current_user.is_admin == 1:
        if Comment.query.filter_by(article_id=article_id).first():
            return '有评论的文章无法删除'
        delete_article = Article.query.filter_by(id=article_id).first()
        db.session.delete(delete_article)
        db.session.commit()
        return '删除成功'
    else:
        return abort(403)
# TODO：完善有评论的文章无法删除


@article.route('/comment_detail/<int:comment_id>')
@login_required
def comment_detail_page(comment_id):
    get_comment = Comment.query.filter_by(id=comment_id).first()
    if get_comment.user.id != current_user.id and current_user.is_admin == 0:
        abort(403)
    else:
        return render_template('/article/comment_detail.html', comment=get_comment)


@article.route('/change_comment/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def change_comment_page(comment_id):
    get_comment = Comment.query.filter_by(id=comment_id).first()
    form = _form.CommentForm()
    if request.method == 'POST' and get_comment.user.id == current_user.id:
        get_comment.title = request.form.get('title')
        get_comment.comment = request.form.get('comment')
        db.session.commit()
        return redirect(url_for('article.comment_detail_page', comment_id=comment_id))
    elif get_comment.user.id == current_user.id:
        return render_template('/article/change_comment.html', comment=get_comment, form=form)
    else:
        abort(403)


@article.route('/delete_comment/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment_page(comment_id):
    get_comment = Comment.query.filter_by(id=comment_id).first()
    if get_comment.user.id != current_user.id and current_user.is_admin == 0:
        abort(403)
    else:
        db.session.delete(get_comment)
        db.session.commit()
    return jsonify({'type': 'success', 'words': '删除成功'})
