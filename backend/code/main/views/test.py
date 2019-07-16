from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.region_record import RegionRecord


class Test(APIView):

    def get(self, request):
        RegionRecord.objects.add_ip('0.0.0.0')
        return Response()
