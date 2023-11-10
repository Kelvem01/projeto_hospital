from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Cliente #Sherlon: Adicionado

# Create your views here.

def ola_mundo(request):
    #return HttpResponse("Olá, Mundo!") #Usando um "html" diretamente no código
    return render(request, 'ola_mundo.html') #Usando um arquivo "html"

def cliente_submit(request):
    if request.POST:
        nome = request.POST.get("nome")     
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        rg = request.POST.get("rg")
        profissao = request.POST.get("profissao")
        
        #Realiza o INSERT no banco de dados
        Cliente.objects.create(
            nome = nome,
            telefone = telefone,
            email = email,
            cpf = cpf,
            rg = rg,
            profissao = profissao
        )
    
    return redirect('/')

def cliente(request):
    clientes = Cliente.objects.all()
    data = {"cliente": clientes}
    return render(request, 'clientes.html', data)