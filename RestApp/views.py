from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from . import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from .models import *

from django.contrib.auth.models import User

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class pruebaGetInfoUser(APIView):
    def get(self,request):
        print(request.user)
        content = {'User':request.user.username}
        return Response(content)

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer