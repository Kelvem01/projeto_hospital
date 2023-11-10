from django.db import models
from django.contrib.auth.models import User #Sherlon: importa a tabela default "User"
from datetime import datetime

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=15, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    profissao = models.CharField(max_length=50, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=True) #Insere a hora atual neste campo

    class Meta: #Força que o nome da tabela seja "evento" e não "core_evento"
        db_table = 'Cliente'
    
    def __str__(self):
        return "class <Cliente>"