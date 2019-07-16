from ._base import BaseModelTest

from ..models.region_record import RegionRecord
from ..models.region import Region


class TestRegionRecord(BaseModelTest):

    ip = '58.128.0.1'
    ip_city_id = 215
    ip_province = '北京'
    ip_city = '北京市'

    def test_add_ip(self):
        # 添加测试数据
        RegionRecord.objects.add_ip(self.ip)
        # 先找到城市
        city = Region.objects.filter(city_id=self.ip_city_id)
        self.assertTrue(city.exists())
        city = city[0]
        self.assertEqual(city.province, self.ip_province)
        self.assertEqual(city.city, self.ip_city)
        # 再判断记录
        record = RegionRecord.objects.filter(region__id=city.id)
        self.assertTrue(record.exists())
        record = record[0]
        self.assertGreater(record.count, 0)
