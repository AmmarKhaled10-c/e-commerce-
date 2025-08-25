from django.shortcuts import render
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny,
    IsAdminUser
)
from .serializers import ProductsSerializers
from .models import Products
from rest_framework import generics

# Create your views here.

class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ProductDetails(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user) 

