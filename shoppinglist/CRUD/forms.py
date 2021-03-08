from django import forms
from django.forms import ModelForm
from .models import Produtos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'quantidade']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder' : 'Produto', 'class' : 'form-control mr-sm-2', 'id': 'idProduto'}),
            'quantidade': forms.TextInput(attrs={'placeholder' : 'Quantidade', 'class' : 'form-control mr-sm-2', 'id': 'idQuantidade'}),            
        }