from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('contatar', views.contatar, name='contatar'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastrar', views.cadastrarUser, name='cadastrar'),
    path('login', views.loginUser, name='login'),
    path('logar', views.logar, name='logar'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logoutUser, name='logout'),
    path('cadastrarProduto', views.cadastrarProduto, name='cadastrarProduto'),
    path('produtos', views.produtos, name='produtos'),
    path('comprar/<int:id_prod>', views.comprar, name='comprar'),
    path('meus-pedidos', views.meus_pedidos, name='meus_pedidos'),
    path('navbar', views.navbar, name='navbar'),
]