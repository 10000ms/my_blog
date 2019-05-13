# -*- coding: utf-8 -*-
import datetime

from django.db import models


class DateRecordManager(models.Manager):

    def _today_record(self):
        c = self.filter(date=datetime.date.today())
        if not c.exists():
            m = self.create()
        else:
            m = c[0]
        return m

    def add_like_count(self):
        m = self._today_record()
        m.like_count += 1
        m.save()

    def add_comment_count(self):
        m = self._today_record()
        m.comment_count += 1
        m.save()

    def add_read_count(self):
        m = self._today_record()
        m.read_count += 1
        m.save()
