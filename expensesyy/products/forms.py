from django import forms

from .models import Product, Receipt

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'receipt'
        ]

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = [
            'shop_name',
        ]