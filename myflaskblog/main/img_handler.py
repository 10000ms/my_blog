# -*- coding: utf-8 -*-
"""
    myflaskblog.main.img_handler
    ~~~~~~~~~

    图片处理模块
    内涵文章，用户头像，网站头像的上传处理相关功能
    页面都无法直接访问

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入需要用到的内置功能
import os
import json
import uuid
from PIL import Image

# 导入flask内的相关类
from flask import Blueprint
from flask import request
from flask import Response
from flask import abort
from flask import current_app
# 导入flask_login模块内检验登陆和获取当前用户类
from flask_login import login_required
from flask_login import current_user

# 导入项目中相关功能
from myflaskblog import db
from myflaskblog.models import Img
from myflaskblog.models import Config


img = Blueprint('img', __name__)


@img.route('/article_img', methods=['POST'])
@login_required
def get_article_img():
    """
    获取文章富文本编辑器上传的图片，并将相关信息存入数据库方便管理

    :return: 图片url地址
    """
    if current_user.is_admin == 1:
        file = request.files['file']
        if file is None:
            abort(404)
        else:
            if file and allowed_file(file.filename):
                # 生成随机文件名
                filename = create_name(file.filename)
                file.save(upload_folder('article_img')+filename)
                new_img = Img(filename)
                db.session.add(new_img)
                db.session.commit()
                img_url = create_img_url('article_img', filename)
                json_res = json.dumps({'errno': 0, 'data': [img_url]})
                res = Response(json_res)
                res.headers["ContentType"] = "text/x-json"
                res.headers["Charset"] = "utf-8"
                return res
    else:
        abort(403)


@img.route('/profile_photo', methods=['POST'])
@login_required
def get_profile_photo():
    """
    获取用户头像，并将相关信息存入数据库方便管理

    :return: ajax功能，返回纯文本信息让前端js获知情况
    """
    if current_user.confirmed:
        file = request.files['profile_photo']
        size = len(file.read())
        if file is None:
            abort(404)
        elif file and allowed_file(file.filename) and size < 1024*1024:
            filename = create_name(file.filename)
            profile_photo_img = change_size(file)
            profile_photo_img.save(upload_folder('profile_photo') + filename)
            # 当用户头像不是默认头像时，删除旧头像
            if current_user.profile_photo != 'Default.jpg':
                old_profile_photo = current_user.profile_photo
                os.remove(upload_folder('profile_photo') + old_profile_photo)
            current_user.profile_photo = filename
            db.session.commit()
            return '上传成功'
    else:
        abort(403)


@img.route('/website_profile_photo', methods=['POST'])
@login_required
def get_website_profile_photo():
    """
    获取网站头像，并将相关信息存入数据库方便管理

    :return: ajax功能，返回纯文本信息让前端js获知情况
    """
    if current_user.confirmed:
        file = request.files['profile_photo']
        size = len(file.read())
        if file is None:
            abort(404)
        elif file and allowed_file(file.filename) and size < 2048*2048:
            filename = create_name(file.filename)
            profile_photo_img = change_website_profile_photo_size(file)
            profile_photo_img.save(upload_folder('website_profile_photo') + filename)
            website_profile = Config.query.filter_by(item='WEBSITE_PROFILE_PHOTO').first().value
            # 当网站头像不是默认头像时，删除旧头像
            if website_profile != 'Default.jpg':
                os.remove(upload_folder('website_profile_photo') + website_profile)
                Config.query.filter_by(item='WEBSITE_PROFILE_PHOTO').first().value = filename
            db.session.commit()
            return '上传成功'
    else:
        abort(403)


def allowed_file(filename):
    """
    文件名的合法性验证

    :param filename:  文件名
    :return:  True为合法；False为非法
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in current_app.config['IMG_ALLOWED_EXTENSIONS']


def upload_folder(func):
    """
    根据不同的功能，生成图片的上传文件夹

    :param func: 功能名
    :return: 文件夹地址
    """
    if func == 'article_img':
        return current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'] + 'article_img/'
    elif func == 'profile_photo':
        return current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'] + 'profile_photo/'
    elif func == 'website_profile_photo':
        return str(current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'])


def create_name(filename):
    """
     获取原文件的格式，生成随机文件名

    :param filename: 原文件名
    :return: 随机文件名
    """
    return str(uuid.uuid1()) + '.' + filename.rsplit('.', 1)[1]


def change_size(img_file):
    """
    生成合适尺寸的用户头像

    :param img_file: 用户上传的图片文件
    :return: 修改尺寸后的图片文件
    """
    img1 = Image.open(img_file)
    return img1.resize((250, 250), Image.ANTIALIAS)


def change_website_profile_photo_size(img_file):
    """
    生成合适尺寸的网站头像

    :param img_file: 上传的原图片文件
    :return: 修改尺寸后的图片文件
    """
    img1 = Image.open(img_file)
    return img1.resize((600, 600), Image.ANTIALIAS)


def create_img_url(func, filename):
    """
    为不同的功能生成相应的图片链接地址

    :param func: 功能名
    :param filename: 文件名
    :return: 图片链接地址
    """
    static_folder = str(current_app.static_folder).rsplit('myflaskblog', 1)[1] + current_app.config['IMG_UPLOAD_FOLDER']
    if func == 'article_img':
        return static_folder + 'article_img/' + filename
    elif func == 'profile_photo':
        return static_folder + 'profile_photo/' + filename
