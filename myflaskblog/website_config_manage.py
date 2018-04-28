# -*- coding: utf-8 -*-
"""
    myflaskblog.redis
    ~~~~~~~~~

    网站设置管理模块
    在网站启动后从数据库

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入项目相关模块
from myflaskblog import app
from myflaskblog.models import Config


def get_website_config():
    """
    从数据库中读取数据进行add_template_global设置，定时任务
    设置内容有：
    1.网站名字
    2.网站备案号
    3.网站头像

    :return:
    """
    with app.app_context():
        if not app.config['APSCHEDULER_LOCK']:
            app.config.update(APSCHEDULER_LOCK=True)
            if Config.query.filter_by(item='WEBSITE_NAME').first():
                website_name = Config.query.filter_by(item='WEBSITE_NAME').first().value
                app.add_template_global(website_name, 'WEBSITE_NAME')
            if Config.query.filter_by(item='WEBSITE_PROFILE_PHOTO').first():
                website_profile_photo_name = str(Config.query.filter_by(item='WEBSITE_PROFILE_PHOTO').first().value)
                website_profile_photo = get_static_url(website_profile_photo_name)
                app.add_template_global(website_profile_photo, 'WEBSITE_PROFILE_PHOTO')
            if Config.query.filter_by(item='WEBSITE_LICENSE').first():
                website_license = Config.query.filter_by(item='WEBSITE_LICENSE').first().value
                app.add_template_global(website_license, 'WEBSITE_LICENSE')
            app.config.update(APSCHEDULER_LOCK=False)
        print('网站默认配置完成')


def get_static_url(img_name):
    """
    网站头像的url地址

    :param img_name: 头像名
    :return: url地址
    """
    static_folder = str(app.static_folder).rsplit('myflaskblog', 1)[1]
    url = static_folder + app.config['IMG_UPLOAD_FOLDER'] + img_name
    return url
