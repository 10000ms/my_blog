from django.db import models

from utils.model_str import str_for_model
from ..manager import date_record


class DateRecord(models.Model):

    date = models.DateField('日期', auto_now=True)
    read_count = models.IntegerField('阅读统计', default=0)
    like_count = models.IntegerField('喜爱统计', default=0)
    comment_count = models.IntegerField('评论统计', default=0)

    objects = date_record.DateRecordManager()

    def __str__(self):
        return str_for_model(self)
