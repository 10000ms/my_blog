# -*- coding: utf-8 -*-
from .settings import *

# docker-compose下，测试的时候celery需要使用正确的测试数据库
test_database = DATABASES['default']['TEST']['NAME']

# 不论如何都关闭DEBUG
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': test_database,
        'USER': secret.DATABASE_ACCOUNT,
        'PASSWORD': secret.DATABASE_PASSWORD,
        'HOST': 'mysql',
        'PORT': '3306',
    }
}
