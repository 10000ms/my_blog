# -*- coding: utf-8 -*-
from django.db import models


class RegionManager(models.Manager):

    def city_from_city_id(self, city_id):
        r = self.filter(city_id=city_id)
        if r.exists():
            return r[0]

    def create_city(self, city_id, city, province, ip):
        pass
