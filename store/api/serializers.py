from rest_framework import serializers
from .models import Item, Size

class SizeSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField()

    class Meta:
        model = Size
        fields = ('title', 'price')

class ItemSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(source='min_price')
    brand_name = serializers.CharField(max_length=20)
    size = SizeSerializer(many=True, source='sizes')

    class Meta:
        model = Item
        fields = ('title', 'sku', 'price', 'brand_name', 'size')
