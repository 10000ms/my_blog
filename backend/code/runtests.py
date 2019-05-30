#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


def main():
    # 使用基本的setting即可
    os.environ['DJANGO_SETTINGS_MODULE'] = 'my_blog.settings'
    django.setup()
    test_runner = get_runner(settings)
    test_runner = test_runner()
    failures = test_runner.run_tests(['main'])
    sys.exit(bool(failures))


if __name__ == '__main__':
    main()
