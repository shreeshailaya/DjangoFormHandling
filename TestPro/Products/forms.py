from django import forms
from .models import ToDoList

class ProductForm(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields=['name','weight','price']