from django.contrib import admin
from core.models import Cliente #Sherlon: Adicionado
from core.models import Anestesista #Sherlon: Adicionado
from core.models import Cirurgiao #Sherlon: Adicionado

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('id', 'nome', 'telefone', 'email', 'cpf', 'rg', 'profissao', 'data_cadastro')

    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome', 'cpf', )

class CirurgiaoAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('id', 'nome', 'telefone', 'email', 'cpf', 'crm', 'data_cadastro')

    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome', 'cpf', 'crm')

class AnestesistaAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('id', 'nome', 'telefone', 'email', 'cpf', 'crm', 'data_cadastro')

    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome', 'cpf', 'crm')

admin.site.register(Cliente, ClienteAdmin) #Sherlon: Adicionado
admin.site.register(Anestesista, AnestesistaAdmin) #Sherlon: Adicionado
admin.site.register(Cirurgiao, CirurgiaoAdmin) #Sherlon: Adicionado