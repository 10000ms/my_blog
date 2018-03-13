#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
文章页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

# 导入模板模块
from flask import render_template

# 导入必要模块
from myflaskblog.models import Article

article = Blueprint('article', __name__)


@article.route('/<int:article_id>')
def article_detail_page(article_id):
    get_article = Article.query.filter_by(id=article_id).first()
    if not get_article:
        return '找不到该文章'

    return render_template("/article/article.html", article=get_article)
