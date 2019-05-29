#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


def main():
    django.setup()
    test_runner = get_runner(settings)
    test_runner = test_runner()
    failures = test_runner.run_tests(['tests'])
    sys.exit(bool(failures))


if __name__ == '__main__':
    main()
