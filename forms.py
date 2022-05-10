from django.core import validators
from django import forms
from .models import User_book

class BookRegistration(forms.ModelForm):
    class Meta:
        model = User_book
        fields = ['book_name','book_author']
        widgets = {
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'book_author': forms.TextInput(attrs={'class': 'form-control'}),

        }
