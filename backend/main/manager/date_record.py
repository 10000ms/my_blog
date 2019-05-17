# -*- coding: utf-8 -*-
from datetime import date, timedelta
from random import randint

from django.db import models


class DateRecordManager(models.Manager):

    def _today_record(self):
        c = self.filter(date=date.today())
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

    def end_index_data(self):
        total = {
            'read_count': self.aggregate(count=models.Sum('read_count'))['count'],
            'like_count': self.aggregate(count=models.Sum('like_count'))['count'],
            'comment_count': self.aggregate(count=models.Sum('comment_count'))['count'],
        }
        seven_day = []
        for d in range(1, 8):
            temp_date = date.today() - timedelta(days=d)
            q = self.filter(date=temp_date)
            # 存在获取真实数据，不存在使用0
            if q.exists():
                read_count = q[0].read_count
                like_count = q[0].like_count
                comment_count = q[0].comment_count
            else:
                read_count = 0
                like_count = 0
                comment_count = 0
            temp_dict = {
                'date': str(temp_date),
                'read_count': read_count,
                'like_count': like_count,
                'comment_count': comment_count,
            }
            seven_day.append(temp_dict)
        r = {
            'total': total,
            'seven_day': seven_day,
        }
        return r

    @staticmethod
    def end_index_demo_data():
        """
        生成demo用的展示数据
        """
        random_read_count = randint(200000, 1000000)
        total = {
            'read_count': random_read_count,
            'like_count': randint(50000, random_read_count),
            'comment_count': randint(50000, random_read_count),
        }
        seven_day = []
        for d in range(1, 8):
            random_day_read_count = randint(500, 2000)
            temp_date = date.today() - timedelta(days=d)
            temp_dict = {
                'date': str(temp_date),
                'read_count': random_day_read_count,
                'like_count': randint(100, random_day_read_count),
                'comment_count': randint(100, random_day_read_count),
            }
            seven_day.append(temp_dict)
        r = {
            'total': total,
            'seven_day': seven_day,
        }
        return r
