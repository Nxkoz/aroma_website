from django import forms

class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Назва')
    aroma = forms.CharField(required=False, label='Аромат')
