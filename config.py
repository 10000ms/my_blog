# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~~~~

    配置模块

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys
import datetime


class ConfigDefault(object):
    """
    默认配置，其他配置均从此配置继承
    """
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/test?charset=utf8'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 跟踪修改，耗费资源，该包作者后期将会取消，False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True  # 使用本地的bootstrap源
    IS_DEVELOPMENT = True  # 自定义值，检查是否出于开发配置环境
    SECRET_KEY = 'oR4NCzUudlWEQwFxcny7zhwib2LTKo8J'  # 配置密匙值，session、cookies及部分其他应用会用到
    PROJECT_PATH = sys.path[0]  # 项目路径

    FLASKY_MAIL_SUBJECT_PREFIX = '1000ms小站信息：'  # 邮件标题名前缀
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')  # 发邮件的人

    MAIL_SERVER = 'smtp.qq.com'  # 发送邮件服务器
    MAIL_PORT = 587  # 使用端口
    MAIL_USE_TLS = True  # 启用安全套接层TLS协议
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # 邮箱登陆用户名，从环境变量中获取
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # 邮箱登陆密码，从环境变量中获取

    IMG_UPLOAD_FOLDER = '/img/'  # 文件上传相关，目录配置
    IMG_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])  # 文件上传相关，允许文件名

    # 定时任务配置
    JOBS = [
        {
            'id': 'get_website_config',
            'func': 'myflaskblog.website_config_manage:get_website_config',
            'trigger': 'interval',
            'seconds': 15,
            'end_date': (datetime.datetime.now() + datetime.timedelta(seconds=20)).strftime('%Y-%m-%d %H:%M:%S'),
        },  # 程序启动后从数据库提取网站设置，执行一次
        {
            'id': 'clear_useless_img',
            'func': 'myflaskblog.img_manage:clear_useless_img',
            'trigger': {'type': 'cron', 'hour': '4'},  # 定时凌晨4点清理无用图片
        }
    ]
    APSCHEDULER_LOCK = False  # 防止定时任务被同时执行多次

    WEBSITE_PROFILE_PHOTO = 'Default.jpg'  # 默认网站头像
    WEBSITE_NAME = '1000ms'  # 默认网站名
    WEBSITE_LICENSE = '备案号-NOT'  # 默认网站备案号

    # REDIS_URL = "redis://:password@localhost:6379/0"
    # REDIS_URL = "unix://[:password]@/path/to/socket.sock?db=0"
    REDIS_URL = "redis://localhost:6379/0"
    REDIS_EXPIRE_TIME = 86400  # redis的key过期时间
    TIME_SPAN = 180  # 登陆用户检查释放时间


class ProductionConfig(ConfigDefault):
    """
    实际工作环境使用配置
    """


class DevelopmentConfig(ConfigDefault):
    """
    开发环境用配置
    """
    DEBUG = True


class TestingConfig(ConfigDefault):
    """
    测试环境用配置
    """
    TESTING = True


# 启动app是调用该处
config = {
    'production_config': ProductionConfig,
    'development_config': DevelopmentConfig,
    'testing_config': TestingConfig,
}
