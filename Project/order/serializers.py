from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductsSerializers

class OrderItemSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')
    product_price = serializers.DecimalField(max_digits=20,decimal_places=2,
                                             source='product.price',read_only=True
                                             )

    class Meta:
        model = OrderItem
        fields = ['order', 'product','product_name','quantity','product_price','item_subtotal']
        extra_kwargs = {'order':{'write_only':True},'product_price':{'write_only':True}}

class OrderSerializers(serializers.ModelSerializer):
    items = OrderItemSerializers(many=True,read_only=True) #nest serializers meaning show the relations
    total_price = serializers.SerializerMethodField()

    def get_total_price(self,obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)


    class Meta:
        model = Order
        fields = ['order_id','user','status','is_paid','paid_at',
                  'order_date','updated_at','total_amount','product','items','total_price']

