from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.
class Products(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=30,decimal_places=3)
    product_description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    active = models.BooleanField(default=False)
    in_stock = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')

    def __str__(self):
        return self.product_name