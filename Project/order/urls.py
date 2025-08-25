from django.urls import path, include
from .views import OrderViews,OrderItemViews,UserOrderViews

urlpatterns = [
    path('list/order/',OrderViews.as_view(),name='list-order'),
    path('order/item/',OrderItemViews.as_view(),name='order-item'),
    path('user/orders/',UserOrderViews.as_view(),name='user-order'),
]