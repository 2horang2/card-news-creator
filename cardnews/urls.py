# cardnews/urls.py
from django.urls import path
from .views import card_list

urlpatterns = [
    path('card-list/', card_list, name='card_list'),
]
