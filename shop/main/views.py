from django.shortcuts import render, redirect
from .models import card, Tag
from .forms import cardForm, UserRegisterForm, AuthUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class LoginFormView(FormView):
    form_class = AuthUserForm
    template_name = "main/user_enter.html"
    success_url = "/"
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class UserRegisterView(CreateView):
    model = User
    template_name = 'main/user.html'
    form_class = UserRegisterForm
    success_url = "/"
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username = username, password = password)
        login(self.request, aut_user)
        return form_valid




class UserLogout(LogoutView):
    next_page = '/'

class PAGE_OF_PRODUCT(DetailView, LoginRequiredMixin):
    model = card
    template_name = 'main/shop.html'
    context_object_name = "card"

class PAGE_OF_UPDATE(UpdateView, LoginRequiredMixin):
    model = card
    template_name = "main/redactor.html"
    form_class = cardForm
    success_url = '/my-ads'

class PAGE_OF_DELETE(DeleteView, LoginRequiredMixin):
    model = card
    success_url = '/my-ads'
    template_name = "main/Delete.html"


def index(request):
    tags = Tag.objects.all()
    cards = card.objects.order_by('-date')
    context = { 'tags': tags, 'cards': cards}
    return render(request, 'main/n1.html', context)

@login_required(login_url='log')
def myads(request):
    cards = card.objects.filter(author=request.user)
    return render(request, "main/index.html", {"title":'Мои объявления', 'cards': cards})

@login_required(login_url='log')
def redactor(request):
    if request.method == 'POST':
        form = cardForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            obj.tags.set(form.cleaned_data.get("tags"))
            form.save_m2m()
            return redirect('/my-ads')
    form = cardForm()
    context = {
        'form': form
    }
    return render(request, "main/redactor.html", context)


def reg(request):
    return render(request, "main/user.html", {'title': 'Регистрация'})

def tag_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    tags = Tag.objects.all()

    return render(request, "main/n1.html", context={'tag':tag, 'tags': tags },)
