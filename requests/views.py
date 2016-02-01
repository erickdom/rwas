from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from requests.models import Request
from requests.serializers import RequestSerializer


class RequestView(APIView):

    def get(self, request, format=None):
        request_sent = Request.objects.all()
        serializer = RequestSerializer(request_sent, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        print request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)