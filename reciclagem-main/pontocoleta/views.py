from django.shortcuts import render
from django.http import HttpResponse

def cadastrarponto(request):
    if request.method == "GET":
        nome = 'Empresa X'
        return render(request, 'cadastrar.html', {'nome': nome})
    elif request.method == "POST":
        nome.request.POST.get('nome')
        endereco.request.POST.get('endereço')
        numero.request.POST.get('numero')
        bairro.request.POST.get('bairro')
        telefone.request.POST.get('telefone')
        return HttpResponse('Cadastro realizado com sucesso!')