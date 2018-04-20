# -*- coding: utf-8 -*-
"""
    myflaskblog.main.index
    ~~~~~~~~~

    博客主页模块
    内含可以直接访问的页面2个：主页和主页文章搜索

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入flask内的相关类
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import make_response

# 导入项目中相关功能
from myflaskblog.models import Article
from myflaskblog.main import _general_method


index = Blueprint('index', __name__)


@index.route('/')
def index_page():
    """
    网站主页，获取文章渲染主页模板

    :return: 渲染/index/index.html
    """
    page = request.args.get('page', 1, type=int)
    all_articles = Article.query.order_by(Article.create_datetime.desc())
    pagination = all_articles.paginate(
        page, per_page=10, error_out=True)
    articles = pagination.items
    need_pagination = _general_method.page_mode(
        len(all_articles.all()),
        len(articles),
        request.args.get('page')
    )
    pagination_url = 'index.index_page'
    return render_template(
        "/index/index.html",
        items=articles,
        pagination=pagination,
        need_pagination=need_pagination,
        pagination_url=pagination_url
    )


@index.route('/search', methods=['GET', 'POST'])
def search_page():
    """
    主页的文章搜索页面
    POST为初次传递搜索关键字，根据关键字查询结果，并将结果存入redis中，方便分页使用
    GET为搜索结果的第二页及之后，提出redis中的关键字，再次进行搜索，输出第二页

    :return: 使用搜索结果的文章渲染/index/index.html
    """
    if request.method == 'POST'and request.form.get('name'):
        search_name = request.form.get('name')
        response = make_response(_general_method.search(
            'Article',
            search_name,
            'index.search_page',
            "/index/index.html",
            request.args.get('page', 1, type=int),
            None
        ))
        # 搜索关键字存入cookie
        response.set_cookie("index_article_search", search_name)
        return response
    elif request.method == 'GET'and request.args.get('page'):
        # 提取搜索关键字，再次进行搜索
        search_name = request.cookies.get('index_article_search')
        return _general_method.search(
            'Article',
            search_name,
            'index.search_page',
            "/index/index.html",
            request.args.get('page', 1, type=int),
            request.args.get('page')
        )
    else:
        return redirect(url_for('index.index_page'))

