from django.test import TestCase
from order.models import Order
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid
from rest_framework import status

User = get_user_model()

# Create your tests here.
class UserOrderTestCase(TestCase):
    def setUp(self) -> None:
        user1 = User.objects.create_user(username='user1',password='test')
        user2 = User.objects.create_user(username='user2',password='test')

        Order.objects.create(user=user1,total_amount='44')
        Order.objects.create(user=user2,total_amount='66')
        Order.objects.create(user=user1,total_amount='22')
        Order.objects.create(user=user2,total_amount='11')
    
    def test_user_order_endpoint_retriveves_only_authenticated_user_order(self):
        user = User.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-order'))

        assert response.status_code == status.HTTP_200_OK
        orders = response.json()
        self.assertTrue(all(uuid.UUID(order['user']) == user.id for order in orders))
    
    def test_user_order_list_unauthenticated(self):
        response = self.client.get(reverse('user-order'))
        self.assertTrue(response.status_code,status.HTTP_401_UNAUTHORIZED)