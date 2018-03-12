#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

# 导入flask扩展
from flask import Flask

# 导入Flask-SQLAlchemy模块
from flask_sqlalchemy import SQLAlchemy

# 导入Flask-bootstrap模块
from flask_bootstrap import Bootstrap

# 导入login模块
from flask_login import LoginManager

# 导入配置模块
from config import config

# 导入其他必要模块
import hashlib


app = Flask(__name__)
app.config.from_object(config['config'])  # 从项目目录的config.py读入配置
db = SQLAlchemy(app)  # 在项目中导入SQLAlchemy模块
bootstrap = Bootstrap(app)  # 在项目中导入bootstrap模块

# 在项目中导入login模块
login_manager = LoginManager()
login_manager.init_app(app)


# 检测当前环境是否处于开发环境，后期改进该测试功能
if app.config['IS_DEVELOPMENT'] and app.config['IS_DEVELOPMENT'] == True :
    # 创建所有数据库表格
    from myflaskblog import models
    db.drop_all()
    db.create_all()
    test_user1 = models.User('123456', '123456', 'VL', '123456@qq.com', 1)
    test_user2 = models.User('111111', '111111', 'VL2', '111111@qq.com')
    db.session.add(test_user1)
    db.session.add(test_user2)
    db.session.commit()
    # TODO:后期改进该测试功能


@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    from myflaskblog.models import User  # 导入user数据库
    user = User.query.filter_by(id=id).first()  # 根据id获取用户信息
    return user  # 没查到的时候filter_by会返回None，符合flask-login要求


# 最后引入防止循环引用
from myflaskblog import main