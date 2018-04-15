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
    pass
