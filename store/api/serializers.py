from rest_framework import serializers

class SizeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=5)
    price = serializers.IntegerField()

class MainSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=25)
    sku = serializers.CharField(max_length=10)
    price = serializers.IntegerField()
    brand_name = serializers.CharField(max_length=20)
    size = SizeSerializer(many=True)
