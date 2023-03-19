from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item

class ItemsListView(generics.ListAPIView):
    queryset = Item.objects.select_related('brand_name').all()
    serializer_class = ItemSerializer
