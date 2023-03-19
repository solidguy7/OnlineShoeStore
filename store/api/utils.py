from django.db.models import QuerySet
from .models import Size, Price

def filter_size_by_item(item: int) -> QuerySet:
    return Size.objects.select_related('item').filter(item=item)

def filter_price_by_size(size: int) -> QuerySet:
    return Price.objects.select_related('size').filter(size=size)
