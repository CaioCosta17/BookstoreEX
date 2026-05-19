import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from product.tests.factories import CategoryFactory, ProductFactory

@pytest.mark.django_db
def test_get_all_products():
    client = APIClient()
    product = ProductFactory()
    
    url = reverse('product-list')
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['title'] == product.title

@pytest.mark.django_db
def test_create_product():
    client = APIClient()
    category = CategoryFactory()
    
    url = reverse('product-list')
    data = {
        "title": "Livro de Django",
        "price": 59.90,
        "category_id": [category.id]
    }
    
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED