# cardnews/views.py
from django.shortcuts import render
from .models import Card

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'cardnews/card_list.html', {'cards': cards})
