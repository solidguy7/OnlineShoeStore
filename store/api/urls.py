from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.ItemsListView.as_view(), name='items_list_view'),
]