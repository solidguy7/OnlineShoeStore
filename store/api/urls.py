from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.GetAllItemsView.as_view(), name='get_all_items_view'),
]