from django.contrib import admin
from .models import Cirurgiao, Anestesista, Especialidade


@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ["nome", "codigo", "is_active"]
    search_fields = ["nome", "codigo"]


@admin.register(Cirurgiao)
class CirurgiaoAdmin(admin.ModelAdmin):
    list_display = ["nome", "crm", "email", "telefone", "is_active"]
    list_filter = ["especialidades", "is_active"]
    search_fields = ["nome", "crm", "cpf"]
    filter_horizontal = ["especialidades"]


@admin.register(Anestesista)
class AnestesistaAdmin(admin.ModelAdmin):
    list_display = ["nome", "crm", "email", "telefone", "is_active"]
    search_fields = ["nome", "crm", "cpf"]
