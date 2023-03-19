from rest_framework import serializers
from .models import Item, Size
from .utils import filter_size_by_item, filter_price_by_size

class SizeSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('get_price')

    class Meta:
        model = Size
        fields = ['title', 'price']

    def get_price(self, obj) -> int:
        for price in filter_price_by_size(obj.id):
            return price.price

class ItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('get_min_price')
    brand_name = serializers.CharField(max_length=20)
    size = SizeSerializer(many=True)

    class Meta:
        model = Item
        fields = ['title', 'sku', 'price', 'brand_name', 'size']

    def get_min_price(self, obj) -> int:
        prices = []
        for size in filter_size_by_item(obj.id):
            for price in filter_price_by_size(size.id):
                prices.append(price.price)
        return min(prices)
