# -*- coding: utf-8 -*-
"""
    myflaskblog.redis
    ~~~~~~~~~

    网站设置管理模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
from myflaskblog import app
from myflaskblog.models import Config


def get_website_config():
    if Config.query.filter_by(item='WEBSITE_NAME').first():
        website_name = Config.query.filter_by(item='WEBSITE_NAME').first().value
        app.add_template_global(website_name, 'WEBSITE_NAME')
    if Config.query.filter_by(item='WEBSITE_PROFILE_PHOTO').first():
        website_profile_photo = \
            app.static_folder \
            + app.config['IMG_UPLOAD_FOLDER'] \
            + str(Config.query.filter_by(item='WEBSITE_PROFILE_PHOTO').first().value)
        app.add_template_global(website_profile_photo, 'WEBSITE_PROFILE_PHOTO')
    if Config.query.filter_by(item='WEBSITE_LICENSE').first():
        website_license = Config.query.filter_by(item='WEBSITE_LICENSE').first().value
        app.add_template_global(website_license, 'WEBSITE_LICENSE')
    print(website_name)
    print(website_profile_photo)
    print(website_license)
