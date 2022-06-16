from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from .models import Livro

# Create your views here.
def index(request):
  return render(request, 'livros/index.html')

def cadastro(request):
  if request.method == 'GET':
    return render(request, 'livros/cadastro.html')
  else:
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = User.objects.filter(username=username).first()

    if user:
      return HttpResponse('Usuário já existe')
    user = User.objects.create_user(
        username=username, email=email, password=senha)
    user.save()
    return redirect('plataforma')

def login(request):
  if request.method == 'GET':
    return render(request, 'livros/login.html')
  else:
    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user = authenticate(username=username, password=senha)
    if(user):
      login_django(request, user)
      return redirect('plataforma')
    else:
      return HttpResponse('Usuário ou senha inválidos')


def plataforma(request):
  livros = Livro.objects.all()
  if request.user.is_authenticated:
    return render(request, 'livros/plataforma.html', {'livros': livros})
  return HttpResponse('Você precisa estar logado')

def cadastro_livro(request):
  if request.method == 'GET':
    return render(request, 'livros/plataforma.html')
  else:
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    ano = request.POST.get('ano')

    livro = Livro.objects.filter(titulo=titulo).first()

    if livro:
      return HttpResponse('Livro já existe')
    livro = Livro.objects.create(
        titulo=titulo, autor=autor, ano=ano)
    livro.save()
    return redirect('plataforma')