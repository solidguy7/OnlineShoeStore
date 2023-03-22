from rest_framework import generics
from django.db.models import Prefetch, Min, Subquery, OuterRef
from .serializers import ItemSerializer
from .models import Item, Size, Price

class ItemsListView(generics.ListAPIView):
    queryset = Item.objects.select_related('brand_name').order_by('title').annotate(
        min_price=Min('sizes__prices__price')).prefetch_related(
        Prefetch('sizes', queryset=Size.objects.annotate(price=Subquery(
            Price.objects.filter(size=OuterRef('pk')).values('price')[:1]))))
    serializer_class = ItemSerializer
