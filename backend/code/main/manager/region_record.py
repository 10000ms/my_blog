# -*- coding: utf-8 -*-
from datetime import date, timedelta
from random import (
    randint,
    sample,
)

from django.db import models

from ip_region import (
    search,
    region_loaction,
)


class RegionRecordManager(models.Manager):

    def _today_record(self, region):
        c = self.filter(date=date.today(), region__id=region.id)
        if not c.exists():
            m = self.create()
            m.region = region
            m.save()
        else:
            m = c[0]
        return m

    def add_ip(self, ip):
        """
        因为可能存在一些未知的情况，所以即使没有成功添加，也不会报错，影响正常使用
        """
        # ip = '58.128.0.1'
        s = search.Ip2Region().search(ip)
        city_id = s['city_id']
        if city_id != 0 and city_id != 1:
            region_manage = self.model.region.field.remote_field.model.objects
            region = region_manage.city_from_city_id(city_id)
            if region is None:
                raw_region_string = s['region'].decode('utf-8')
                region_list = raw_region_string.split('|')
                province = region_list[2]
                city = region_list[3]
                region = region_manage.create_city(city_id, city, province, ip)
            if region is not None:
                m = self._today_record(region)
                m.count += 1
                m.save()

    def end_index_data(self):
        today = date.today()
        seven_day = self.filter(date__range=[today - timedelta(days=7), today])
        return seven_day\
            .values('region__city', 'region__lat', 'region__lng')\
            .annotate(count=models.Sum('count'))\
            .order_by('region__city')

    @staticmethod
    def _demo_data_model(city, lat, lng):
        """
        生成demo用的展示单条数据
        """
        return {
            'region__city': city,
            'region__lat': lat,
            'region__lng': lng,
            'count': randint(2, 50),
        }

    def end_index_demo_data(self):
        """
        生成demo用的展示数据集合
        """
        key = region_loaction.demo_location.keys()
        choice_city = sample(list(key), 40)
        res = []
        for c in choice_city:
            d = region_loaction.demo_location[c]
            res.append(self._demo_data_model(c, d[1], d[0]))
        return res
