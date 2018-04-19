# -*- coding: utf-8 -*-
"""
    myflaskblog.main._generalMethod
    ~~~~~~~~~

    通用功能模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入Serializer加密
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 导入flask内的模板渲染和当前app功能
from flask import render_template
from flask import current_app

# 导入项目数据库及相关表
from myflaskblog import db
from myflaskblog.models import Article
from myflaskblog.models import User
from myflaskblog.models import Comment


def page_mode(all_item_len, page_item_len, page=None, each_page_item=10):
    """
    检测数据库资源数量，确定是否加载pagination页码模块以及“没有喽~”模块。
    1.首页未满10个资源不加载pagination页码模块
    2.判断是否在最后一页，在则加载“没有喽~”模块（部分页面用到）

    :param all_item_len: 所有数据库该项资源数量
    :param page_item_len: 本页资源数量
    :param page: 页码
    :param each_page_item: 每页资源的数量
    :return: 0：无pagination页码模块，有“没有喽~”模块；
              1：有pagination页码模块，有“没有喽~”模块；
              2：有pagination页码模块，无“没有喽~”模块；
    """
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


def search(search_model, search_name, pagination_url, template, pagination_page, page):
    """
    搜索模块，用来解决资源搜索及后续页码处理，目前有：Article，User，Comment的搜索

    :param search_model: 要进行搜索的model类
    :param search_name: 用户要搜索的字段
    :param pagination_url: 页面pagination所需要指向的url
    :param template: 所需要渲染的模板
    :param pagination_page: pagination所需要的page参数
    :param page: 页码
    :return: 直接使用的渲染模板
    """
    if search_model == 'Article':
        search_item = Article.query.filter(Article.title.ilike('%' + search_name + '%'))
    elif search_model == 'User':
        search_item = User.query.filter(User.is_admin != 1, User.username.ilike('%' + search_name + '%'))
    elif search_model == 'Comment':
        search_item = Comment.query.filter(Comment.title.ilike('%' + search_name + '%'))
    pagination = search_item.paginate(pagination_page, per_page=10, error_out=True)
    pagination_items = pagination.items
    need_pagination = page_mode(
        len(search_item.all()),
        len(pagination_items),
        page
    )
    return render_template(
        template,
        items=pagination_items,
        pagination=pagination,
        need_pagination=need_pagination,
        pagination_url=pagination_url
    )


def check_token(token, function_module):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    if function_module == 'confirm':
        fm_name = 'c'
        if User.query.filter_by(id=data.get(fm_name)).first():
            check_user = User.query.filter_by(id=data.get(fm_name)).first()
            if not check_user.confirmed:
                check_user.confirmed = True
                db.session.commit()
                return data.get(fm_name)
            else:
                return False
        else:
            return False
