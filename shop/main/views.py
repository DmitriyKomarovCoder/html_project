from django.shortcuts import render
from .models import card


def index(request):
    cards = card.objects.all()
    return render(request, 'main/n1.html', {'title': 'Главная страница', 'cards': cards})


def myads(request):
    cards = card.objects.all()
    return render(request, "main/index.html", {"title":'Мои объявления', 'cards': cards})


def ad(request):
    return render(request, "main/shop.html", {"title": card.title})