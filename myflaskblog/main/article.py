# -*- coding: utf-8 -*-
"""
    myflaskblog.main.article
    ~~~~~~~~~

    博客文章处理模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入蓝图模块
from flask import Blueprint

# 导入模板模块
from flask import render_template

# 导入必要模块
from myflaskblog.models import Article, Comment
from myflaskblog import db
from flask import redirect, abort, flash
from myflaskblog import img_manage
from myflaskblog.main import _form
from flask import request, url_for
from flask import jsonify
from myflaskblog.img_manage import get_profile_photo_folder

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user


article = Blueprint('article', __name__)


@article.route('/<int:article_id>', methods=['GET', 'POST'])
def article_detail_page(article_id):
    get_article = Article.query.filter_by(id=article_id).first()
    form = _form.CommentForm()
    if not get_article:
        return '找不到该文章'
    elif form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        user_id = current_user.id
        article_id = article_id
        new_comment = Comment(title, comment, user_id, article_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('评论成功')
        return redirect(url_for('article.article_detail_page', article_id=article_id))
    else:
        page = request.args.get('page', 1, type=int)
        get_comment = Comment.query.filter_by(article_id=article_id)
        pagination = get_comment.order_by(Comment.create_datetime.desc()).paginate(
            page, per_page=5, error_out=True)
        comments = pagination.items
        if len(get_comment.all()) > 5:
            if len(comments) < 5:
                need_pagination = 1
            elif request.args.get('page') and int(request.args.get('page')) * 10 == len(get_comment.all()):
                need_pagination = 1
            else:
                need_pagination = 2
        else:
            need_pagination = 0
        folder = get_profile_photo_folder()
        return render_template("/article/article.html", article=get_article, form=form, comments=comments, \
                               pagination=pagination, need_pagination=need_pagination, folder=folder)


@article.route('/new_article', methods=['GET', 'POST'])
@login_required
def new_article_page():
    if request.method == 'POST' and current_user.is_admin == 1:
        new_article_title = request.form.get('title')
        if not new_article_title:
            return '出错了'
        new_article_keyword = request.form.get('title')
        new_article_description = request.form.get('description')
        new_article_content = request.form.get('content')
        new_article_user_id = current_user.id
        new_article = Article(new_article_title, new_article_keyword, new_article_description, new_article_content, \
                              new_article_user_id)
        db.session.add(new_article)
        db.session.commit()
        img_manage.img_add_article_id(new_article.id, new_article.content)
        return url_for('article.article_detail_page', article_id=new_article.id)
    elif current_user.is_admin == 1:
        form = _form.ArticleForm()
        return render_template('/article/new_article.html', form=form)
    else:
        abort(403)


@article.route('/manage_article')
@login_required
def manage_article_page():
    if current_user.is_admin == 1:
        page = request.args.get('page', 1, type=int)
        all_articles = Article.query.order_by(Article.create_datetime.desc())
        pagination = all_articles.paginate(page, per_page=10, error_out=True)
        articles = pagination.items
        if len(all_articles.all()) > 10:
            if len(articles) < 10:
                need_pagination = 1
            elif request.args.get('page') and int(request.args.get('page')) * 10 == len(all_articles.all()):
                need_pagination = 1
            else:
                need_pagination = 2
        else:
            need_pagination = 0
        return render_template("/article/manage_article.html", articles=articles, pagination=pagination, need_pagination=need_pagination)
    else:
        abort(403)


@article.route('/search', methods=['POST'])
def search_article_page():
    if current_user.is_admin == 1:
        if request.method == 'POST'and request.form.get('name'):
            search_name = request.form.get('name')
            search_articles = Article.query.filter(Article.title.ilike('%'+search_name+'%'))
            page = request.args.get('page', 1, type=int)
            pagination = search_articles.paginate(page, per_page=10, error_out=True)
            articles = pagination.items
            if len(search_articles.all()) > 10:
                if len(articles) < 10:
                    need_pagination = 1
                elif request.args.get('page') and int(request.args.get('page')) * 10 == len(search_articles.all()):
                    need_pagination = 1
                else:
                    need_pagination = 2
            else:
                need_pagination = 0
            return render_template("/article/manage_article.html", articles=articles, pagination=pagination, need_pagination=need_pagination)
        else:
            return redirect(url_for('article.manage_article_page'))
    else:
        abort(403)
    # TODO:换页问题，redis储存上次搜索


@article.route('/change_article/<int:article_id>', methods=['GET', 'POST'])
@login_required
def change_article_page(article_id):
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
        delete_article = Article.query.filter_by(id=article_id).first()
        db.session.delete(delete_article)
        db.session.commit()
        return '删除成功'
    else:
        return abort(403)


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
    if form.validate_on_submit() and get_comment.user.id == current_user.id:
        get_comment.title = form.title.data
        get_comment.comment = form.comment.data
        db.session.commit()
        flash('修改成功')
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

# TODO:评论有更好的处理方法
