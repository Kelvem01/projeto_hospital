from django.contrib import admin
from .models import Paciente, Convenio


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "cpf", "email", "telefone", "convenio", "is_active"]
    list_filter = ["convenio", "is_active"]
    search_fields = ["nome", "cpf", "email"]


@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ["nome", "codigo", "telefone", "is_active"]
    search_fields = ["nome", "codigo"]
