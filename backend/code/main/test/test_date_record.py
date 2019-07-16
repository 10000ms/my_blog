from datetime import date

from ._base import BaseModelTest
from ..models.date_record import DateRecord


class TestDateRecord(BaseModelTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.today_record = None

    def setUp(self):
        super().setUp()
        # 获取今天的记录
        self.today_record = DateRecord.objects.today_record()

    def test_today_record(self):
        """
        测试是否正确获取今天记录，这对测试很重要
        """
        self.assertEqual(self.today_record.date, date.today())
