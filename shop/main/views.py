from django.shortcuts import render, redirect
from .models import card
from .forms import cardForm, UserLogForm, UserRegisterForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
class UserLoginView(LoginView):
    template_name = 'main/user_enter.html'
    form_class = UserLogForm
    success_url = ''

class UserRegisterView(CreateView):
    model = User
    template_name = 'main/user.html'
    form_class = UserRegisterForm
    success_url = '/'
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = self.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username = username, password = password)
        login(self.request, aut_user)
        return form_valid


class UserLogout(LogoutView):
    next_page = '/'

class PAGE_OF_PRODUCT(DetailView):
    model = card
    template_name = 'main/shop.html'
    context_object_name = "card"

class PAGE_OF_UPDATE(UpdateView):
    model = card
    template_name = "main/redactor.html"
    form_class = cardForm
    success_url = '/my-ads'
class PAGE_OF_DELETE(DeleteView):
    model = card
    success_url = '/my-ads'
    template_name = "main/Delete.html"


def index(request):
    cards = card.objects.order_by('-date')
    return render(request, 'main/n1.html', {'title': 'Главная страница', 'cards': cards})


def myads(request):
    cards = card.objects.all()
    return render(request, "main/index.html", {"title":'Мои объявления', 'cards': cards})





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


