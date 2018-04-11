# -*- coding: utf-8 -*-
"""
    myflaskblog.main.index
    ~~~~~~~~~

    博客主页模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入蓝图模块
from flask import Blueprint

# 导入模板模块
from flask import render_template

# 导入必要的模块
from myflaskblog.models import User, Article
from flask import request, url_for, redirect, abort


index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def index_page():
    page = request.args.get('page', 1, type=int)
    all_articles = Article.query.order_by(Article.create_datetime.desc())
    pagination = all_articles.paginate(
        page, per_page=10, error_out=True)
    articles = pagination.items
    if len(all_articles.all()) > 10:
        if len(articles) < 10:
            need_pagination = 1
        elif request.args.get('page') and int(request.args.get('page'))*10 == len(all_articles.all()):
            need_pagination = 1
        else:
            need_pagination = 2
    else:
        need_pagination = 0
    return render_template("/index/index.html", articles=articles, pagination=pagination, need_pagination=need_pagination)


@index.route('/search', methods=['POST'])
def search_page():
    if request.method == 'POST'and request.form.get('name'):
        search_name = request.form.get('name')
        search_articles = Article.query.filter(Article.title.ilike('%'+search_name+'%'))
        page = request.args.get('page', 1, type=int)
        pagination = search_articles.paginate(page, per_page=10, error_out=True)
        articles = pagination.items
        if len(search_articles.all()) > 10:
            if len(articles) < 10:
                need_pagination = 1
            elif request.args.get('page') and request.args.get('page') * 10 != len(search_articles.all()):
                need_pagination = 1
            else:
                need_pagination = 2
        else:
            need_pagination = 0
        return render_template("/index/index.html", articles=articles, pagination=pagination, need_pagination=need_pagination)
    else:
        return redirect(url_for('index.index_page'))
    # TODO:换页问题，redis储存上次搜索
