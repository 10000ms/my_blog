#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
flask project entrance.
'''

import os

# 导入SQLite
from sqlite3 import dbapi2 as sqlite3

# 导入flask扩展
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# 创建SQLite
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# 创建Flask应用程序实例
# 需要传入__name__，作用是确定资源所在的路径
app = Flask(__name__)

# 定义路由及视图函数
# Flask中定义路由是由专门的路由装饰器实现的
@app.route("/")
def hello():
    return "Hello World!"

# 启动程序
if __name__ == '__main__':
    app.run()