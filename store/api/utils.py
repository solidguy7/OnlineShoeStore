from typing import List
from django.db.models import QuerySet
from .models import Item, Size, Price

def get_size_keys() -> List:
    size_price, size_title, result = [], [], []
    for ind, size_obj in enumerate(get_size()):
        for price_obj in filter_price_by_size(ind):
            size_price.append(price_obj.price)
            break
        size_title.append(size_obj.title)
        result.append({'title': size_title[ind], 'price': size_price[ind]})
    return result

def get_min_price() -> int:
    size_price = []
    for ind, size_obj in enumerate(get_size()):
        for price_obj in filter_price_by_size(ind):
            size_price.append(price_obj.price)
            break
    return min(size_price)

def get_item_title() -> str:
    item_title = None
    for item_obj in get_item():
        item_title = item_obj.title
    return item_title

def get_item_sku() -> str:
    item_sku = None
    for item_obj in get_item():
        item_sku = item_obj.sku
    return item_sku

def get_item_brand_name() -> str:
    item_brand_name = None
    for item_obj in get_item():
        item_brand_name = item_obj.brand_name
    return item_brand_name

def get_item() -> QuerySet:
    return Item.objects.select_related('brand_name').all()

def get_size() -> QuerySet:
    return Size.objects.select_related('item').all()

def filter_price_by_size(size: int) -> QuerySet:
    return Price.objects.select_related('size').filter(size=size)
