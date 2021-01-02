from .models import card
from django.forms import ModelForm, TextInput, Textarea

class cardForm(ModelForm):
    class Meta:
        model = card
        fields = ["title", "description"]
        widgets = {
                "title": TextInput(attrs={
                    "class": 'form-control',
                    'placeholder': "Краткое название отражающее суть"
            }),
                "description": Textarea(attrs={
                    "class": 'form-control',
                    'placeholder': 'Подробно опишите всю информацию о товаре'
            })

        }