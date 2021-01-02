from django.shortcuts import render, redirect
from .models import card
from .forms import cardForm


def index(request):
    cards = card.objects.all()
    return render(request, 'main/n1.html', {'title': 'Главная страница', 'cards': cards})


def myads(request):
    cards = card.objects.all()
    return render(request, "main/index.html", {"title":'Мои объявления', 'cards': cards})


def ad(request):
    return render(request, "main/shop.html", {"title": 'Объявление'})


def redactor(request):
    if request.method == 'POST':
        form = cardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my-ads')
    form = cardForm()
    context = {
        'form': form
    }
    return render(request, "main/redactor.html", context)

def reg(request):
    return render(request, "main/user.html", {'title': 'Регистрация'})

def enter(request):
    return render(request, "main/user_enter.html", {'title': 'Войти'})


