# -*- coding: utf-8 -*-
"""
    myflaskblog.redis
    ~~~~~~~~~

    redis管理模块
    用于协助网站使用
    记录用户搜索，确定单点登陆，并在登出时清除记录
    还用于确定最新的邮箱认证token和发送间隔

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
# 导入时间模块进行计时
from time import time
# 导入Serializer进行解密
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 导入flask相关的功能
from flask import current_app

# 导入项目相关模块
from myflaskblog import redis_store
from myflaskblog.models import User


def add_redis_user_data(user_id, func, value):
    """
    在redis中增加和用户相关的记录，一般用于搜索分页功能

    :param user_id: 用户id
    :param func: 功能模块
    :param value: 储存值
    :return:
    """
    expire_time = current_app.config['REDIS_EXPIRE_TIME']
    redis_name = str(user_id) + str(func)
    if redis_store.get(redis_name):
        redis_store.delete(redis_name)
    redis_store.set(redis_name, value, expire_time)


def get_redis_user_value(user_id, func):
    """
    在redis中查找和用户相关的记录，一般用于搜索分页功能

    :param user_id: 用户id
    :param func: 功能模块
    :return: 储存的值
    """
    redis_name = str(user_id) + str(func)
    value = str(redis_store.get(redis_name))[2:]
    value = value[:-1]
    return value


def user_login_out(user_id):
    """
    用户登出时清除redis中用户有关的记录
    能清除功能模块：
    1.article.search_article_page（文章管理中的文章搜索）
    2.admin.search_user_page（用户管理中的用户搜索）
    3.admin.search_comment_page（管理中的评论搜索）
    4.session （用户session，单点登陆用）
    5.session_time（用户session时间，单点登陆用）

    :param user_id: 登出用户id
    :return:
    """
    article_redis_name = str(user_id) + 'article.search_article_page'
    if redis_store.get(article_redis_name):
        redis_store.delete(article_redis_name)
    user_redis_name = str(user_id) + 'admin.search_user_page'
    if redis_store.get(user_redis_name):
        redis_store.delete(user_redis_name)
    comment_redis_name = str(user_id) + 'admin.search_comment_page'
    if redis_store.get(comment_redis_name):
        redis_store.delete(comment_redis_name)
    redis_session_name = str(user_id) + 'session'
    redis_session_time = str(user_id) + 'session_time'
    redis_store.delete(redis_session_name)
    redis_store.delete(redis_session_time)


def check_send_time(user_id):
    """
    检测记录用户发送邮件时间，防止频发发送邮件

    :param user_id: 发送邮件的用户id
    :return:
    """
    expire_time = current_app.config['REDIS_EXPIRE_TIME']
    email_redis_name = str(user_id) + 'email'
    time_value = int(time())
    if redis_store.get(email_redis_name):
        old_time_value = str(redis_store.get(email_redis_name))[2:]
        old_time_value = int(old_time_value[:-1])
        if int(time()) - old_time_value < 60:
            return False
        else:
            redis_store.set(email_redis_name, time_value, expire_time)
            return True
    else:
        redis_store.set(email_redis_name, time_value, expire_time)
        return True


def email_token_set(user_id, token):
    """
    将最新的认证邮件的token信息记录，防止多个验证邮件或邮箱都可以认证

    :param user_id: 用户id
    :param token: 用于验证的token
    :return:
    """
    expire_time = current_app.config['REDIS_EXPIRE_TIME']
    email_token_redis_name = str(user_id) + 'email_token'
    if redis_store.get(email_token_redis_name):
        redis_store.delete(email_token_redis_name)
    redis_store.set(email_token_redis_name, token, expire_time)


def email_token_check(token):
    """
    检验认证token是否正确并与最新的token相同

    :param token:
    :return: 通过验证返回True，不通过返回False
    """
    # 先检验认证token是否正确
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    if User.query.filter_by(id=data.get('c')).first():
        user_id = User.query.filter_by(id=data.get('c')).first().id
    else:
        return False
    # 再检测认证的token是否和redis中储存的一致
    # redis中没有，但认证token正确时，返回True，防止因重启服务器导致的redis数据清空
    email_token_redis_name = str(user_id) + 'email_token'
    if redis_store.get(email_token_redis_name):
        redis_token = str(redis_store.get(email_token_redis_name))[2:]
        redis_token = redis_token[:-1]
        if redis_token == token:
            return True
        else:
            return False
    else:
        return True


def user_session_set(user_id, session):
    """
    单点登陆模块：用户session设置
    记录用户的session和session时间

    :param user_id: 用户id
    :param session: session值
    :return:
    """
    expire_time = current_app.config['REDIS_EXPIRE_TIME']
    redis_session_name = str(user_id) + 'session'
    redis_session_time = str(user_id) + 'session_time'
    if redis_store.get(redis_session_name):
        redis_store.delete(redis_session_name)
    if redis_store.get(redis_session_time):
        redis_store.delete(redis_session_time)
    redis_store.set(redis_session_name, session, expire_time)
    redis_store.set(redis_session_time, int(time()), expire_time)


def user_session_check(user_id, session):
    """
    单点登陆模块：用户session和session时间检测，设置，更新

    :param user_id: 用户id
    :param session: session值
    :return:
    """
    time_span = current_app.config['TIME_SPAN']
    redis_session_name = str(user_id) + 'session'
    redis_session_time = str(user_id) + 'session_time'
    # 检测是否储存该用户session值，没有就设置
    if redis_store.get(redis_session_name) and redis_store.get(redis_session_time):
        # 检测新旧session区别，旧session和当前session相同则仅更新session时间
        old_session = str(redis_store.get(redis_session_name))[2:]
        old_session = old_session[:-1]
        if old_session != session:
            last_time = str(redis_store.get(redis_session_time))[2:]
            last_time = int(last_time[:-1])
            # 检测上次操作时间，大于时间间隔设置新session
            if int(time()) - last_time < time_span:
                return False
            else:
                # 设置session和session的时间
                user_session_set(user_id, session)
                return True
        else:
            # 设置session和session的时间
            user_session_set(user_id, session)
            return True
    else:
        # 设置session和session的时间
        user_session_set(user_id, session)
        return True
