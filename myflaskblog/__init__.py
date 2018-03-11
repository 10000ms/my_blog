#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

# 导入flask扩展
from flask import Flask

# 导入Flask-SQLAlchemy模块
from flask_sqlalchemy import SQLAlchemy

# 导入Flask-bootstrap模块
from flask_bootstrap import Bootstrap

# 导入配置模块
from config import config

app = Flask(__name__)
app.config.from_object(config['config'])  #从config.py读入配置
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


# 检测当前环境是否处于开发环境，后期改进该测试功能
if app.config['IS_DEVELOPMENT'] and app.config['IS_DEVELOPMENT'] == True :
    # 创建所有数据库表格
    from myflaskblog import models
    db.drop_all()
    db.create_all()
    # TODO:后期改进该测试功能

# 最后引入防止循环引用
from myflaskblog import main