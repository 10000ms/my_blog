# -*- coding: utf-8 -*-
"""
    myflaskblog.redis
    ~~~~~~~~~

    redis管理模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
from myflaskblog import redis_store
from flask import current_app
from time import time
from myflaskblog.models import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def add_redis_user_data(user_id, func, value):
    expire_time = current_app.config['REDIS_EXPIRE_TIME']
    redis_name = str(user_id) + str(func)
    if redis_store.get(redis_name):
        redis_store.delete(redis_name)
    redis_store.set(redis_name, value, expire_time)


def get_redis_user_value(user_id, func):
    redis_name = str(user_id) + str(func)
    value = str(redis_store.get(redis_name))[2:]
    value = value[:-1]
    return value


def user_login_out(user_id):
    article_redis_name = str(user_id) + 'article.search_article_page'
    if redis_store.get(article_redis_name):
        redis_store.delete(article_redis_name)
    user_redis_name = str(user_id) + 'admin.search_user_page'
    if redis_store.get(user_redis_name):
        redis_store.delete(user_redis_name)
    comment_redis_name = str(user_id) + 'admin.search_comment_page'
    if redis_store.get(comment_redis_name):
        redis_store.delete(comment_redis_name)
    email_redis_name = str(user_id) + 'email'
    if redis_store.get(email_redis_name):
        redis_store.delete(email_redis_name)
    redis_session_name = str(user_id) + 'session'
    redis_session_time = str(user_id) + 'session_time'
    redis_store.delete(redis_session_name)
    redis_store.delete(redis_session_time)


def check_send_time(user_id):
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
    expire_time = current_app.config['REDIS_EXPIRE_TIME']
    email_token_redis_name = str(user_id) + 'email_token'
    if redis_store.get(email_token_redis_name):
        redis_store.delete(email_token_redis_name)
    redis_store.set(email_token_redis_name, token, expire_time)


def email_token_check(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    if User.query.filter_by(id=data.get('c')).first():
        user_id = User.query.filter_by(id=data.get('c')).first().id
    else:
        return False
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
    time_span = current_app.config['TIME_SPAN']
    redis_session_name = str(user_id) + 'session'
    redis_session_time = str(user_id) + 'session_time'
    if redis_store.get(redis_session_name) and redis_store.get(redis_session_time):
        last_time = str(redis_store.get(redis_session_time))[2:]
        last_time = int(last_time[:-1])
        if int(time()) - last_time < time_span:
            old_session = str(redis_store.get(redis_session_name))[2:]
            old_session = old_session[:-1]
            if old_session == session:
                user_session_set(user_id, session)
                return True
            else:
                return False
        else:
            user_session_set(user_id, session)
            return True
    else:
        user_session_set(user_id, session)
        return True
