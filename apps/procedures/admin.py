from django.contrib import admin
from .models import Procedimento


@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ["codigo_interno", "nome", "codigo_tuss", "valor_base", "is_active"]
    list_filter = ["especialidade", "is_active"]
    search_fields = ["nome", "codigo_interno", "codigo_tuss"]
