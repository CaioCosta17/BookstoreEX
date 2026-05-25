from rest_framework import serializers
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer
from product.models.category import Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True, source='category'
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'active', 'category', 'category_id']