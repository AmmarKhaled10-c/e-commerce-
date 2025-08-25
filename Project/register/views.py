from django.shortcuts import render
from .serializers import RegisterSerializers
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth import get_user_model

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]

    def get_queryset(self):
        User = get_user_model()
        return User.objects.all()