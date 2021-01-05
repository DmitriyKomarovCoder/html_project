from .models import card
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class cardForm(ModelForm):
    class Meta:
        model = card
        fields = ["title", "description", 'price', "image", 'annotation']
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
            })


        }

class UserLogForm(ModelForm, AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    widgets = {
        "username": TextInput(attrs={
            "class": 'form-control',
            'placeholder': "Краткое название отражающее суть"
        }),
        "password": TextInput(attrs={
            "class": 'form-control',
            'placeholder': "Краткое название отражающее суть"
        }),
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLogForm, self).__init__(*args, **kwargs)

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
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