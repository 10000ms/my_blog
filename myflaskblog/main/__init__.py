# -*- coding: utf-8 -*-
"""
    myflaskblog.main.__init__
    ~~~~~~~~~

    蓝图注册模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入项目本身
from myflaskblog import app


# 导入各个路由模块
from .index import index
from .admin import admin
from .article import article
from .user import user
from .img_handler import img
from .error import error_handler


# 注册蓝图
app.register_blueprint(index)  # url_prefix='/admin' 是以/admin或者/user的情况下才会通过注册的蓝图的视图方法处理请求并返回
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(article, url_prefix='/article')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(img, url_prefix='/img')
app.register_blueprint(error_handler)


