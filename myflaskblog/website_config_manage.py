# -*- coding: utf-8 -*-
"""
    myflaskblog.redis
    ~~~~~~~~~

    网站设置管理模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
from flask import url_for
from myflaskblog import app
from myflaskblog.models import Config


def get_website_config():
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


def get_static_url(img_name):
    static_folder = str(app.static_folder).rsplit('myflaskblog', 1)[1]
    url = static_folder + app.config['IMG_UPLOAD_FOLDER'] + img_name
    return url
