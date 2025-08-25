from django.shortcuts import render
from rest_framework import generics
from .models import Order,OrderItem
from django.contrib.auth import get_user_model
from .serializers import OrderItemSerializers,OrderSerializers
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

User = get_user_model()

class OrderViews(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializers
    permission_classes = [AllowAny]

class UserOrderViews(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #overwrite on Query to make it for specific user that order this items
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)

class OrderItemViews(generics.CreateAPIView):
    serializer_class = OrderItemSerializers
    permission_classes = [AllowAny]
