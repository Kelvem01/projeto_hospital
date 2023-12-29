from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import * #Sherlon: Adicionado (Importa classes Cliente, Cirurgiao, etc)

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
    data = {"dados": clientes}
    return render(request,'listarDados.html', data)

"""Renderiza a página de cadastro de Cirurgioes"""
def cirurgiao(request):
    cirurgioes = Cirurgiao.objects.all()
    data = {"cirurgiao": cirurgioes}
    return render(request, 'cirurgioes.html', data)

"""Adiciona o cirurgiao ou anestesista cadastrado no banco de dados"""
def cirurgiao_submit(request):
    if request.POST:
        nome = request.POST.get("nome")     
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        crm = request.POST.get("crm")
        
        #Realiza o INSERT no banco de dados
        Cirurgiao.objects.create(
            nome = nome,
            telefone = telefone,
            email = email,
            cpf = cpf,
            crm = crm
        )
    
    return redirect('/')

"""Apresenta os cirurgioes cadastrados no sistema"""
def listar_cirurgioes(request):
    cirurgioes = Cirurgiao.objects.all()
    cirurgioes = cirurgioes.order_by('nome')
    data = {"dados": cirurgioes}
    return render(request,'listarDados.html', data)

"""Renderiza a página de cadastro de Anestesistas"""
def anestesista(request):
    anestesistas = Anestesista.objects.all()
    data = {"anestesista": anestesistas}
    return render(request, 'anestesistas.html', data)

def anestesista_submit(request):
    if request.POST:
        nome = request.POST.get("nome")     
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        crm = request.POST.get("crm")
        
        #Realiza o INSERT no banco de dados
        Anestesista.objects.create(
            nome = nome,
            telefone = telefone,
            email = email,
            cpf = cpf,
            crm = crm
        )
    
    return redirect('/')

"""Apresenta os anestesistas cadastrados no sistema"""
def listar_anestesistas(request):
    anestesistas = Anestesista.objects.all()
    anestesistas = anestesistas.order_by('nome')
    data = {"dados": anestesistas}
    return render(request,'listarDados.html', data)