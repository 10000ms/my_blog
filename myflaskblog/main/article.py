#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
文章页路由模块
'''

# 导入蓝图模块
from flask import Blueprint

# 导入模板模块
from flask import render_template

# 导入必要模块
from myflaskblog.models import Article

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user

# 导入WTF模块
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

# 上传图片所需要的模块
import os
from flask import request, Response, url_for
import json
from myflaskblog import app

article = Blueprint('article', __name__)


@article.route('/<int:article_id>')
def article_detail_page(article_id):
    get_article = Article.query.filter_by(id=article_id).first()
    if not get_article:
        return '找不到该文章'

    return render_template("/article/article.html", article=get_article)


@article.route('/new_article', methods=['GET', 'POST'])
@login_required
def new_article_page():
    if request.method == 'POST':
        new_article = request.form.get('title')
        # TODO;正确处理收到的文章，并返回信息
    else:
        now_login_user = current_user
        if now_login_user.is_admin == 1:
            form = ArticleForm(request.form)
            return render_template('/article/new_article.html', form=form)
        elif now_login_user.is_admin == 0:
            return '没有权限'


# 文章上传图片部分

UPLOAD_FOLDER = app.config['PROJECT_PATH'] + '/myflaskblog/static/ImageUploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@article.route('/img', methods=['POST'])
@login_required
def get_img():
    file = request.files['file']
    if file == None:
        result = r"error|未成功获取文件，上传失败"
        res = Response(result)
        res.headers["ContentType"] = "text/x-json"
        res.headers["Charset"] = "utf-8"
        return res
    else:
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(UPLOAD_FOLDER+filename)
            img_url = url_for('static', filename='ImageUploads/'+filename)
            jsonres = json.dumps({'errno': 0, 'data': [img_url]})
            res = Response(jsonres)
            res.headers["ContentType"] = "text/x-json"
            res.headers["Charset"] = "utf-8"
            return res
    # TODO:后期重新封装并实现检查,对于static的使用亦要处理，wangediotr传过来多张图片亦要想办法处理

# TODO：增加对无用图片的检查功能


# 文件名合法性验证
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


class ArticleForm(FlaskForm):
    title = StringField('标题', [DataRequired('标题必填！'), Length(min=6, max=20, message='账户必须介于6-20字符！')])
    keyword = StringField('关键词', [DataRequired('关键词必填！'), Length(min=6, max=20, message='密码必须介于6-20字符！')])
    description = StringField('描述', [DataRequired('描述必填！'), Length(min=6, max=100, message='密码必须介于6-20字符！')])
    content = StringField('正文', [DataRequired('正文必填！')])
