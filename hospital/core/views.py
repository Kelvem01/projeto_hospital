from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Cliente #Sherlon: Adicionado

# Create your views here.

def home(request):
    return render(request, "index.html")

def ola_mundo(request):
    #return HttpResponse("Olá, Mundo!") #Usando um "html" diretamente no código
    return render(request, 'ola_mundo.html') #Usando um arquivo "html"

"""Adiciona o cliente cadastrado no banco de dados"""
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

"""Renderiza a página de cadastro de Clientes"""
def cliente(request):
    clientes = Cliente.objects.all()
    data = {"cliente": clientes}
    return render(request, 'clientes.html', data)

"""Apresenta os clientes cadastrados no sistema"""
def listar_clientes(request):
    clientes = Cliente.objects.all()
    clientes = clientes.order_by('nome')
    data = {"clientes": clientes}
    return render(request,'listarClientes.html', data)