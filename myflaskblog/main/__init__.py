# -*- coding: utf-8 -*-
"""
    myflaskblog.main.__init__
    ~~~~~~~~~

    蓝图注册模块
    注册蓝图：/；/admin；/article；/user；/img
    以及全局错误模块
    所有模块均在myflaskblog.main内

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入项目本身
from myflaskblog import app

# 导入各个路由模块
from myflaskblog.main.index import index
from myflaskblog.main.admin import admin
from myflaskblog.main.article import article
from myflaskblog.main.user import user
from myflaskblog.main.img_handler import img
from myflaskblog.main.error import error_handler


# 注册蓝图
app.register_blueprint(index)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(article, url_prefix='/article')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(img, url_prefix='/img')
app.register_blueprint(error_handler)


