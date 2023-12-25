from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput
from django import forms
from .models import Product, Photo 


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["productName", "description", "price"]
        widgets = {
            "productName": TextInput(attrs={'class': 'form-control'}),
            "description": Textarea(attrs={'class': 'form-control'}),
            "price": NumberInput(attrs={'class': 'form-control'}),
        }

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
        widgets = {
            'image': FileInput(attrs={'class': 'form-control'}),
        }


