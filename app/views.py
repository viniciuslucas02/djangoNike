from django.shortcuts import render, redirect
from app.models import Contato, Produto, Pedido, Pagina
from app.forms import FormUsuario, FormProduto, FormCompra
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    pagina = Pagina.objects.first()
    produtos = Produto.objects.all().values()[:4]
    return render(request, 'index.html', {'pagina': pagina, 'produtos': produtos})


def navbar (request):
    pagina = Pagina.objects.first()
    return render(request, 'navbar.html', {'pagina': pagina})

def contato (request):
    pagina = Pagina.objects.first()
    return render(request, 'contato.html',  {'pagina': pagina})

def contatar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
        return redirect('/')
    return render(request, "contato.html")



def cadastro(request):
    formulario = FormUsuario(request.POST or None)
    pagina = Pagina.objects.first()
    context = {
        'form': formulario,
        'pagina': pagina
    }
    return render(request, 'cadastroUser.html', context)

def cadastrarUser(request):
    form = FormUsuario(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect ('index')
    return render(request, 'cadastroUser.html', {'form': form})



def loginUser(request):
    return render(request, 'login.html')

def logar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect ('/')
        else:
            messages.error(request, 'Nome ou senha inválidos.')

    return render(request, 'login.html')




@login_required(login_url='logar')
def dashboard(request):
    if not request.user:
        return redirect('irlogin')
    return render(request, 'dashboard.html', {'usuario': request.user})

def logoutUser(request):
    logout(request)
    return redirect('/')



def cadastrarProduto(request):
    if request.POST:
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormProduto()
    return render(request, 'cadastroProduto.html', {'form': form})


def produtos(request):
    if not request.user:
        return redirect('irlogin')
    produtos = Produto.objects.all().values()
    return render(request, 'produtos.html', {'produtos': produtos})

@login_required(login_url='logar')
def comprar(request, id_prod):
    produto = Produto.objects.get(id=id_prod)
    if request.method == 'POST':
        form = FormCompra(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.produto = produto

            if compra.quantidade > produto.estoque:
                messages.error(request, 'Quantidade solicitada excede o estoque disponível.')
                return redirect('produtos')
            
            produto.estoque -= compra.quantidade
            produto.save()
            compra.save()
            Pedido.objects.create(
                usuario=request.user,
                produto=produto,
                quantidade=1
    )

            messages.success(request, 'Compra realizada com sucesso!')

            return redirect('produtos')
    else:
        form = FormCompra()
    return render(request, 'comprar.html', {'form': form, 'produto': produto})

@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'pedidos.html', {'pedidos': pedidos})
