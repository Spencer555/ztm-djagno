from django.urls import path 
from link_plant.views import LinkListView, LinkCreateView, LinkUpdateView, LinkDeleteView, profile_view


urlpatterns = [
    path('', LinkListView.as_view(), name='link_lists'),
    path('create/', LinkCreateView.as_view(), name='link-create'), 
    path('update/<int:pk>/', LinkUpdateView.as_view(), name='link-update'),
    path('delete/<int:pk>/', LinkDeleteView.as_view(), name='link-delete'),
    path('profile/<slug:profile_slug>/', profile_view, name='profile'),
]
