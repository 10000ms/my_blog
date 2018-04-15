# -*- coding: utf-8 -*-
"""
    myflaskblog.main._generalMethod
    ~~~~~~~~~

    通用功能模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
from myflaskblog.models import Article
from flask import request
from flask import render_template


def page_mode(all_item_len, page_item_len, page=None, each_page_item=10):
    if all_item_len > each_page_item:
        if page_item_len < each_page_item:
            need_pagination = 1
        elif page and int(page)*each_page_item == all_item_len:
            need_pagination = 1
        else:
            need_pagination = 2
    else:
        need_pagination = 0
    return need_pagination


def search_article(search_name, pagination_url, template):
    search_articles = Article.query.filter(Article.title.ilike('%' + search_name + '%'))
    page = request.args.get('page', 1, type=int)
    pagination = search_articles.paginate(page, per_page=10, error_out=True)
    articles = pagination.items
    need_pagination = page_mode(
        len(search_articles.all()),
        len(articles),
        request.args.get('page')
    )
    return render_template(
        template,
        articles=articles,
        pagination=pagination,
        need_pagination=need_pagination,
        pagination_url=pagination_url
    )
