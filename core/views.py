from rest_framework import settings
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer
from .models import UserModel
from rest_framework.response import Response
from django.conf import settings


class GetAllUserList(APIView):
    def get(self,request):
        query = UserModel.objects.all()
        serializer = UserSerializer(query,many=True)
        serializer_data = sorted(serializer.data, key = lambda i: i['quests_status'],reverse=True)[0:20]
        return Response(serializer_data,status=200)
