# -*- coding: utf-8 -*-
import datetime

from django.db import models


class DateRecordManager(models.Manager):

    def _today_record(self):
        m = self.filter(date=datetime.date.today())
        if not m.exists():
            m = self.create()
        return m

    def add_like_count(self):
        m = self._today_record()
        m.like_count += 1
        m.save()

    def add_comment_count(self):
        m = self._today_record()
        m.comment_count += 1
        m.save()
