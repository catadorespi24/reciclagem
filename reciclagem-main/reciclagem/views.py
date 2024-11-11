from django.shortcuts import render
from django.http import HttpResponse

def adicionarproduto(request):
    if request.method == "GET":
        nome = 'Produto'
        return render(request, 'cadastrarproduto.html', {'nome': nome})
    elif request.method == "POST":
        produto.request.POST.get('produto')
        descricao.request.POST.get('descrição')
        categoria.request.POST.get('categoria')
        return HttpResponse('Cadastro realizado com sucesso!')