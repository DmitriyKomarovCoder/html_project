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


def redactor(request):
    return render(request, "main/redactor.html", {'title': 'Редактор'})

def reg(request):
    return render(request, "main/user.html", {'title': 'Регистрация'})

def enter(request):
    return render(request, "main/user_enter.html", {'title': 'Войти'})

