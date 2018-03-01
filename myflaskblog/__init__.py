#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

# 导入flask扩展
from flask import Flask

# 导入Flask-SQLAlchemy模块
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")  #从config.py读入配置
db = SQLAlchemy(app)


# 最后引入防止循环引用
from myflaskblog import main