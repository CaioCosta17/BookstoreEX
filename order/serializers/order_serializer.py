from rest_framework import serializers
from order.models.order import Order
from product.serializers.product_serializer import ProductSerializer
from product.models.product import Product

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True, source='product'
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'product_id']