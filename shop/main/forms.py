from .models import card, Tag
from django import forms
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, CharField, SelectMultiple
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class cardForm(ModelForm):
    class Meta:
        model = card
        fields = ["title", "description", 'price', "image", 'annotation', 'phone', 'tags']
        widgets = {
                "title": TextInput(attrs={
                    "class": 'form-control',
                    'placeholder': "Краткое название отражающее суть"
            }),
                "description": Textarea(attrs={
                    "class": 'form-control',
                    'placeholder': 'Подробно опишите всю информацию о товаре'
            }),
                "annotation": Textarea(attrs={
                    "class": 'form-control',
                    'placeholder': 'Краткая аннотация, которая заинтересует покупателя'
            }),
                "phone": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Введите ваш номер телефона начиная с 8'
            }),
                "tags": SelectMultiple(attrs={
                "class": 'form-control'
            })

        }

class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]
        widgets = {
            "username": TextInput(attrs={
                "class": 'form-control',
                'placeholder': "Введите имя пользователя"
            }),
            "password": TextInput(attrs={
                "class": 'form-control',
                'placeholder': "пароль"
            }),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


