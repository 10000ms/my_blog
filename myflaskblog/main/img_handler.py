#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
图片处理模块
'''

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user

# 导入蓝图模块
from flask import Blueprint


# 导入必要模块
from myflaskblog.models import Img
from myflaskblog import db
from flask import redirect, abort, flash, current_app
import os
from flask import request, Response, url_for
import json
from myflaskblog import app
import uuid
from PIL import Image

img = Blueprint('img', __name__)


@img.route('/article_img', methods=['POST'])
@login_required
def get_article_img():
    if current_user.is_admin == 1:
        file = request.files['file']
        if file is None:
            abort(404)
        else:
            if file and allowed_file(file.filename):
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
    # TODO:wangediotr传过来多张图片要想办法处理

# TODO：增加对无用图片的检查功能


@img.route('/profile_photo', methods=['POST'])
@login_required
def get_profile_photo():
    if current_user.is_admin == 1:
        file = request.files['profilephoto']
        size = len(file.read())
        if file is None:
            abort(404)
        elif file and allowed_file(file.filename) and size < 1024*1024:
            filename = create_name(file.filename)
            profile_photo_img = change_size(file)
            profile_photo_img.save(upload_folder('profile_photo') + filename)
            if current_user.profile_photo != 'Default.jpg':
                old_profile_photo = current_user.profile_photo
                os.remove(upload_folder('profile_photo') + old_profile_photo)
            current_user.profile_photo = filename
            db.session.commit()
            return '上传成功'
    else:
        abort(403)


# 文件名合法性验证
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['IMG_ALLOWED_EXTENSIONS']


# 生成上传文件夹
def upload_folder(func):
    if func == 'article_img':
        return current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'] + 'article_img/'
    elif func == 'profile_photo':
        return current_app.static_folder + current_app.config['IMG_UPLOAD_FOLDER'] + 'profile_photo/'


# 生成随机文件名
def create_name(filename):
    return str(uuid.uuid1()) + '.' + filename.rsplit('.', 1)[1]


# 生成合适尺寸的图片
def change_size(img_file):
    img1 = Image.open(img_file)
    return img1.resize((250, 250), Image.ANTIALIAS)


# 生成链接地址
def create_img_url(func, filename):
    if func == 'article_img':
        return url_for('static', filename='img/article_img/'+filename)
    elif func == 'profile_photo':
        return url_for('static', filename='img/profile_photo/' + filename)
