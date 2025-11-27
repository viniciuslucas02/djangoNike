from django import forms
from app.models import Categoria, Produto, Compra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
         
         
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-[#1e1801] focus:outline-none',
                'placeholder': 'Seu nome de usuário'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-[#1e1801] focus:outline-none',
                'placeholder': 'Seu email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-[#1e1801] focus:outline-none',
                'placeholder': 'Senha'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-[#1e1801] focus:outline-none',
                'placeholder': 'Confirme a senha'
            }),
        }


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'imagem', 'categoria', 'estoque']

        widgets = {
            'descricao': forms.TextInput(attrs={'placeholder': 'seu nome aqui'}),
            'imagem' : forms.FileInput(attrs={'accept': 'imagem/*'})
        }

class FormCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['quantidade']