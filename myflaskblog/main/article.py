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

# 上传图片所需要的模块
import os
from flask import request, Response, url_for
import json

article = Blueprint('article', __name__)


@article.route('/<int:article_id>')
def article_detail_page(article_id):
    get_article = Article.query.filter_by(id=article_id).first()
    if not get_article:
        return '找不到该文章'

    return render_template("/article/article.html", article=get_article)



# 文章上传图片部分

UPLOAD_FOLDER = '/TmageUploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@article.route('/img', methods=['POST'])
@login_required
def get_img():
    file = request.files[0]
    if file == None:
        result = r"error|未成功获取文件，上传失败"
        res = Response(result)
        res.headers["ContentType"] = "text/x-json"
        res.headers["Charset"] = "utf-8"
        return res
    else:
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            img_url = url_for('article.get_img') + filename
            jsonres = json.dumps({'errno': 0, 'data': [img_url]})
            res = Response(img_url)
            res.headers["ContentType"] = "text/x-json"
            res.headers["Charset"] = "utf-8"
            return res
    # TODO:后期重新封装并实现检查


# 文件名合法性验证
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS