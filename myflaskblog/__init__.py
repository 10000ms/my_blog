#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    myflaskblog.__init__
    ~~~~~~~~~

    项目初始模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
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

# 导入Mail模块
from flask_mail import Mail

# 导入定时任务模块
from flask_apscheduler import APScheduler

# 导入Redis模块
from flask_redis import FlaskRedis

# 导入其他必要模块
import hashlib


app = Flask(__name__)
app.config.from_object(config['config'])  # 从项目目录的config.py读入配置
db = SQLAlchemy(app)  # 在项目中导入SQLAlchemy模块
bootstrap = Bootstrap(app)  # 在项目中导入bootstrap模块
mail = Mail(app)  # 在项目中导入mail模块
redis_store = FlaskRedis(app)  # 在项目中导入Redis模块

# 在项目中导入login模块
login_manager = LoginManager()
login_manager.init_app(app)

# 在项目中创建定时任务
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


# 检测当前环境是否处于开发环境，后期改进该测试功能
if app.config['IS_DEVELOPMENT']:
    # 创建所有数据库表格
    from myflaskblog import models
    db.drop_all()
    db.create_all()
    test_user1 = models.User('123456', 'a123456', 'VL', '111111@qq.com', True, True)
    test_user2 = models.User('111111', 'a111111', 'VL2', '111111@qq.com', False, True)
    test_user3 = models.User('111112', 'a111111', 'VL3', '111111@qq.com', False, False)
    test_user4 = models.User('111114', '111111', 'VL4', '111111@qq.com')
    test_user5 = models.User('111115', '111111', 'VL5', '111111@qq.com')
    test_user6 = models.User('111116', '111111', 'VL6', '111111@qq.com')
    test_user7 = models.User('111117', '111111', 'VL7', '111111@qq.com')
    test_user8 = models.User('111118', '111111', 'VL8', '111111@qq.com')
    test_user9 = models.User('111119', '111111', 'VL9', '111111@qq.com')
    test_user10 = models.User('1111110', '111111', 'VL10', '111111@qq.com')
    test_user11 = models.User('1111111', '111111', 'VL11', '111111@qq.com')
    test_article1 = models.Article('A1', 'kw', 'not', '这是一篇博文', 1)
    test_article2 = models.Article('A2', 'kw', 'not', '这是一篇博文', 1)
    test_article3 = models.Article('A3', 'kw', 'not', '这是一篇博文', 1)
    test_article4 = models.Article('A4', 'kw', 'not', '这是一篇博文', 1)
    test_article5 = models.Article('A5', 'kw', 'not', '这是一篇博文', 1)
    test_article6 = models.Article('A6', 'kw', 'not', '这是一篇博文', 1)
    test_article7 = models.Article('A7', 'kw', 'not', '这是一篇博文', 1)
    test_article8 = models.Article('A8', 'kw', 'not', '这是一篇博文', 1)
    test_article9 = models.Article('A9', 'kw', 'not', '这是一篇博文', 1)
    test_article10 = models.Article('A10', 'kw', 'not', '这是一篇博文', 1)
    test_article11 = models.Article('A11', 'kw', 'not', '这是一篇博文', 1)
    test_article12 = models.Article('A12', 'kw', 'not', '这是一篇博文', 1)
    test_article13 = models.Article('A13', 'kw', 'not', '这是一篇博文', 1)
    test_article14 = models.Article('A14', 'kw', 'not', '这是一篇博文', 1)
    test_article15 = models.Article('A15', 'kw', 'not', '这是一篇博文', 1)
    test_article16 = models.Article('A16', 'kw', 'not', '这是一篇博文', 1)
    test_article17 = models.Article('A17', 'kw', 'not', '这是一篇博文', 1)
    test_article18 = models.Article('A18', 'kw', 'not', '这是一篇博文', 1)
    test_article19= models.Article('A19', 'kw', 'not', '这是一篇博文', 1)
    test_article20 = models.Article('A20', 'kw', 'not', '这是一篇博文', 1)
    test_config1 = models.Config('WEB_SITE_PROFILE_PHOTO', '111.jpg')
    test_config2 = models.Config('WEB_SITE_NAME', '1000ms')
    db.session.add(test_user1)
    db.session.add(test_user2)
    db.session.add(test_user3)
    db.session.add(test_user4)
    db.session.add(test_user5)
    db.session.add(test_user6)
    db.session.add(test_user7)
    db.session.add(test_user8)
    db.session.add(test_user9)
    db.session.add(test_user10)
    db.session.add(test_user11)
    db.session.add(test_article1)
    db.session.add(test_article2)
    db.session.add(test_article3)
    db.session.add(test_article4)
    db.session.add(test_article5)
    db.session.add(test_article6)
    db.session.add(test_article7)
    db.session.add(test_article8)
    db.session.add(test_article9)
    db.session.add(test_article10)
    db.session.add(test_article11)
    db.session.add(test_article12)
    db.session.add(test_article13)
    db.session.add(test_article14)
    db.session.add(test_article15)
    db.session.add(test_article16)
    db.session.add(test_article17)
    db.session.add(test_article18)
    db.session.add(test_article19)
    db.session.add(test_article20)
    db.session.add(test_config1)
    db.session.add(test_config2)
    db.session.commit()
    # TODO:后期改进该测试功能


@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    from myflaskblog.models import User  # 导入user数据库
    user = User.query.filter_by(id=id).first()  # 根据id获取用户信息
    return user  # 没查到的时候filter_by会返回None，符合flask-login要求


# 设置模板全局变量
app.add_template_global(app.config['WEB_SITE_NAME'], 'WEB_SITE_NAME')
app.add_template_global(app.static_folder + app.config['IMG_UPLOAD_FOLDER']+app.config['WEB_SITE_PROFILE_PHOTO'], \
                        'WEB_SITE_PROFILE_PHOTO')


# 最后引入防止循环引用
from myflaskblog import main