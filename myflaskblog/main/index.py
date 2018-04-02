#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
主页路由模块
'''

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
    pagination = Article.query.order_by(Article.create_datetime.desc()).paginate(
        page, per_page=10, error_out=True)
    articles = pagination.items
    return render_template("/index/index.html", articles=articles, pagination=pagination)


@index.route('/search', methods=['POST'])
def search_page():
    if request.method == 'POST'and request.form.get('name'):
        search_name = request.form.get('name')
        search_articles = Article.query.filter(Article.title.ilike('%'+search_name+'%'))
        page = request.args.get('page', 1, type=int)
        pagination = search_articles.paginate(page, per_page=10, error_out=True)
        articles = pagination.items
        return render_template("/index/index.html", articles=articles, pagination=pagination)
    else:
        return redirect(url_for('index.index_page'))



