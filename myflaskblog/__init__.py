#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    myflaskblog.__init__
    ~~~~~~~~~

    项目初始模块
    初始化项目，配置设置及一些而外模块
    最后导入路由main

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入flask内的相关类
from flask import Flask
# 导入flask扩展类
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_apscheduler import APScheduler  # 定时任务
from flask_redis import FlaskRedis
from flask_script import Manager
from flask_script import Shell
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

# 导入本项目需要模块
from config import config


app = Flask(__name__)
app.config.from_object(config['config'])  # 从项目目录的config.py读入配置
db = SQLAlchemy(app)  # 在项目中导入SQLAlchemy模块
bootstrap = Bootstrap(app)  # 在项目中导入bootstrap模块
mail = Mail(app)  # 在项目中导入mail模块
redis_store = FlaskRedis(app)  # 在项目中导入Redis模块
manager = Manager(app)  # 在项目中导入shell管理功能
migrate = Migrate(app, db)  # 数据库迁移功能

# 在项目中导入login模块
login_manager = LoginManager()
login_manager.init_app(app)

# 在项目中创建定时任务
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


# 创建完成后再导入models类
from myflaskblog import models


def make_shell_context():
    """
    为shell建立上下文环境

    :return:
    """
    return dict(
        app=app,
        db=db,
        User=models.User,
        Config=models.Config,
        Article=models.Article,
        Comment=models.Comment,
        Img=models.Img,
    )


# 增加shell指令
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.option('-d', '-drop_first', dest='drop_first', default=False)
def create_db(drop_first):
    """
    数据库初始化命令
    python manage.py create_db -d True 清空数据库

    :param drop_first: 是否清空久数据库，默认否
    :return:
    """
    if drop_first:
        db.drop_all()
    db.create_all()
    super_user = models.User('123456', 'a123456', 'VL', '111111@qq.com', True, True)
    website_config_set_1 = models.Config('WEBSITE_PROFILE_PHOTO', '111.jpg')
    website_config_set_2 = models.Config('WEBSITE_NAME', '1000ms的小站')
    website_config_set_3 = models.Config('WEBSITE_LICENSE', '备案号：暂无')
    db.session.add(super_user)
    db.session.add(website_config_set_1)
    db.session.add(website_config_set_2)
    db.session.add(website_config_set_3)
    db.session.commit()
    redis_store.flushdb()  # 清空当前redis数据库
    print("ok")


@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    from myflaskblog.models import User  # 导入user数据库
    user = User.query.filter_by(id=id).first()  # 根据id获取用户信息
    return user  # 没查到的时候filter_by会返回None，符合flask-login要求


# 设置模板全局变量
app.add_template_global(app.config['WEBSITE_NAME'], 'WEBSITE_NAME')
app.add_template_global(app.config['WEBSITE_LICENSE'], 'WEBSITE_LICENSE')
app.add_template_global('/static/img/'+app.config['WEBSITE_PROFILE_PHOTO'],
                        'WEBSITE_PROFILE_PHOTO')


# 最后引入防止循环引用
from myflaskblog import main