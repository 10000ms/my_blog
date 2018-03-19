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
from myflaskblog.models import Article, Comment
from myflaskblog import db
from flask import redirect, abort

# 导入flask_login模块
from flask_login import login_user, login_required, logout_user, current_user

# 导入WTF模块
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
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
    form = CommentForm(article_id)
    return render_template("/article/article.html", article=get_article, form=form, article_id=article_id)


@article.route('/new_article', methods=['GET', 'POST'])
@login_required
def new_article_page():
    if request.method == 'POST':
        new_article_title = request.form.get('title')
        if not new_article_title:
            return '出错了'
        new_article_keyword = request.form.get('title')
        new_article_description = request.form.get('title')
        new_article_content = request.form.get('title')
        new_article = Article(new_article_title, new_article_keyword, new_article_description, new_article_content)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('index.index_page'))
    else:
        now_login_user = current_user
        if now_login_user.is_admin == 1:
            form = ArticleForm(request.form)
            return render_template('/article/new_article.html', form=form)
        elif now_login_user.is_admin == 0:
            return '没有权限'


@article.route('/add_comment', methods=['POST'])
@login_required
def add_comment_page():
    form = CommentForm(request.form)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        user_id = current_user.id
        article_id = form.article_id.data
        new_comment = Comment(title, comment, user_id, article_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('article.article_detail_page', article_id=article_id))
    else:
        abort(404)




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
    title = StringField('标题', [DataRequired('标题必填！'), Length(min=6, max=20, message='标题必须介于6-20字符！')])
    keyword = StringField('关键词', [DataRequired('关键词必填！'), Length(min=6, max=20, message='关键词必须介于6-20字符！')])
    description = StringField('描述', [DataRequired('描述必填！'), Length(min=6, max=100, message='描述必须介于6-20字符！')])
    content = StringField('正文', [DataRequired('正文必填！')])


class CommentForm(FlaskForm):
    title = StringField('标题', [DataRequired('标题必填！'), Length(min=6, max=20, message='账户必须介于6-20字符！')])
    comment = StringField('评论', [DataRequired('评论必填！')])
    article_id = HiddenField(default=1)
    submit = SubmitField('提交')
    # TODO：article_id字段正确获取






