from django.shortcuts import render
from rest_framework import generics,permissions
from .serializer import UserSerializer
# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer