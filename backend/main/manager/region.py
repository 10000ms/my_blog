# -*- coding: utf-8 -*-
import requests

from django.db import models
from django.conf import settings

from utils.logging import logger


class RegionManager(models.Manager):

    url_string = 'http://api.map.baidu.com/geocoder/v2/?address={}{}&output=json&ak={}'

    def city_from_city_id(self, city_id):
        r = self.filter(city_id=city_id)
        if r.exists():
            return r[0]

    def create_city(self, city_id, city, province, ip):
        s = requests.get(self.url_string.format(province, city, settings.BAIDU_AK))
        r = s.json()
        status = r['status']
        if status == 0:
            r_res = r['result']['location']
            instance = self.create(province=province, city=city, city_id=city_id, lat=r_res['lat'], lng=r_res['lng'])
            return instance
        else:
            logger.warning('error ip: <{}>, status: <{}>, msg: <{}>'.format(ip, status, r['message']))
