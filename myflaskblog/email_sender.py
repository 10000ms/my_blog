# -*- coding: utf-8 -*-
"""
    myflaskblog.email_sender
    ~~~~~~~~~

    email发送功能模块

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入线程
from threading import Thread

# 导入flask内的相关类
from flask import current_app
from flask import render_template
# 导入flask_mail中的信息功能
from flask_mail import Message

# 导入项目邮件功能
from myflaskblog import mail


def send_async_email(app, msg):
    """
    发送邮件线程导入项目

    :param app: 项目
    :param msg: 邮件信息
    :return:
    """
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    """
    邮件组合及建立线程

    :param to: 发送给
    :param subject: 邮件主题
    :param template: 邮件模板
    :param kwargs: 其他参数
    :return: 该邮件发送线程
    """
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
