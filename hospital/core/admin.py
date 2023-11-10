from django.contrib import admin
from core.models import Cliente #Sherlon: Adicionado

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('id', 'nome', 'telefone', 'email', 'cpf', 'rg', 'profissao', 'data_cadastro')

    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome', 'cpf', )

admin.site.register(Cliente, ClienteAdmin) #Sherlon: Adicionado