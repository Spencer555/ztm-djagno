from django.urls import path 
from .views import item_list, item_list_serialized, item_detail, item_list_rest


urlpatterns = [
    path('', item_list, name='home'),
    path('home_rest/', item_list_rest, name='home-rest'),
    path('home_serialized/', item_list_serialized, name='home_serialized'),
    path('item-detail/<int:pk>/', item_detail, name='item-detail'),
]
