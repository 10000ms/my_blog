# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.user import User
from ..serializers.user import UserSerializer


class MainIndex(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(user, many=True, context=serializer_context)
        print(serializer.data)
        return Response(serializer.data)
