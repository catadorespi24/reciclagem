from django.shortcuts import render
from django.http import HttpResponse
from .models import CadastroUsuario

def cadastro(request):
    if request.method == "GET":
        nome = 'Rodrigo'
        return render(request, 'cadastro.html', {'nome': nome})
    elif request.method == "POST":
        nome.request.POST.get('nome')
        apelido.request.POST.get('apelido')
        telefone.request.POST.get('telefone')
        senha.request.POST.get('senha')
        confirme_senha.request.POST.get('Confirmação de Senha')
        return HttpResponse('Cadastro realizado com sucesso!')


def login(request):
    if request.method == "GET":
        nome = 'Rodrigo'
        return render(request, 'login.html', {'nome': nome})
    elif request.method == "POST":
        apelido.request.POST.get('apelido')
        senha.request.POST.get('senha')
        return HttpResponse('Login realizado com sucesso!')