from django import forms
from biasharaapp.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'origin', 'color', 'description']



