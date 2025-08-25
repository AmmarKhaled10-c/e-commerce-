from products.models import Products
from order.models import Order,OrderItem
from django.db import connection

def run():
    order = OrderItem.objects.filter(user_id__exact='aba9db5afff6402fad3bcc99278cd3eb')

    print(order)

    # print(connection.queries)
