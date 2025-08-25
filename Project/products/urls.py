from django.urls import path
from .views import ProductsListCreateAPIView,ProductDetails

urlpatterns = [
    path('products/',ProductsListCreateAPIView.as_view(),name='products'),
    path('product/<uuid:product_id>/',ProductDetails.as_view()),
]