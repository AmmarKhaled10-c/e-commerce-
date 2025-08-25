from rest_framework import serializers
from .models import Products

class ProductsSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Products
        fields = ['id','product_name', 'price','product_description', 'active','in_stock','user']
        extra_kwarg = {'id':{'read_only':True}}