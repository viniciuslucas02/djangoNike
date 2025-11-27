from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.CharField(max_length=255)

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.produto.preco * self.quantidade


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.produto.nome}"
    
    def total(self):
        return self.produto.preco * self.quantidade


class Pagina(models.Model):
    nome_Site = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pagina/', null=True, blank=True)
    texto_chamada = models.CharField(max_length=255)
    texto_sobre = models.CharField(max_length=1024)
    imagem_sobre = models.ImageField(upload_to='pagina/', null=True, blank=True)
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.IntegerField()
    criado_em = models.DateField(auto_now_add=True)