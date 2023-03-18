from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializers import MainSerializer, SizeSerializer
from .utils import get_item_title, get_item_sku, get_item_brand_name, get_min_price, get_size_keys

class GetAllItemsView(views.APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        size_serializer = SizeSerializer(get_size_keys(), many=True)
        item = {'title': get_item_title(), 'sku': get_item_sku(), 'price': get_min_price(),
                'brand_name': get_item_brand_name(), 'size': size_serializer.data}
        main_serializer = MainSerializer(item)
        return Response(main_serializer.data, status=HTTP_200_OK)
