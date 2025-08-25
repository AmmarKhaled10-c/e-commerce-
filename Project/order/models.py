from django.db import models
from products.models import Products
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.
class Order(models.Model):
    class StatusChoises(models.TextChoices):
        PENDING = 'Pending'
        PAID = 'Paid'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)   
    status = models.CharField(max_length=15,choices=StatusChoises,default=StatusChoises.PENDING)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True,blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.PositiveIntegerField()

    product = models.ManyToManyField(Products,through="OrderItem", related_name='orders')

    def __str__(self):
        return f"order {self.order_id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    
    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Order {self.order.order_id}"




