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
from myflaskblog.models import Article
from flask import url_for
from flask import redirect
from flask import request
from flask import make_response
from myflaskblog.main import _generalMethod


index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def index_page():
    page = request.args.get('page', 1, type=int)
    all_articles = Article.query.order_by(Article.create_datetime.desc())
    pagination = all_articles.paginate(
        page, per_page=10, error_out=True)
    articles = pagination.items
    need_pagination = _generalMethod.page_mode(
        len(all_articles.all()),
        len(articles),
        request.args.get('page')
    )
    pagination_url = 'index.index_page'
    return render_template(
        "/index/index.html",
        articles=articles,
        pagination=pagination,
        need_pagination=need_pagination,
        pagination_url=pagination_url
    )


@index.route('/search', methods=['GET', 'POST'])
def search_page():
    if request.method == 'POST'and request.form.get('name'):
        search_name = request.form.get('name')
        response = make_response(_generalMethod.search_article(search_name, 'index.search_page', "/index/index.html"))
        response.set_cookie("index_article_search", search_name)
        return response
    elif request.method == 'GET'and request.args.get('page'):
        search_name = request.cookies.get('index_article_search')
        return _generalMethod.search_article(search_name, 'index.search_page', "/index/index.html")
    else:
        return redirect(url_for('index.index_page'))

