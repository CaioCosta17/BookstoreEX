import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from product.tests.factories import ProductFactory
from order.models.order import Order

@pytest.mark.django_db
def test_create_order():
    client = APIClient()
    
    user = User.objects.create_user(username='testuser', password='123')
    token = Token.objects.create(user=user)
    
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
    product = ProductFactory()
    url = reverse('order-list')
    data = {
        "user": user.id,
        "product_id": [product.id]
    }
    
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED