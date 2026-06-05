from django.contrib import admin
from .models import InsightIA, Dashboard, Indicador


@admin.register(InsightIA)
class InsightIAAdmin(admin.ModelAdmin):
    list_display = ["tipo", "titulo", "data_referencia", "created_at"]
    list_filter = ["tipo", "data_referencia"]
    search_fields = ["titulo", "descricao"]


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ["nome", "tipo", "is_active"]
    list_filter = ["tipo"]


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ["nome", "chave", "valor_atual", "unidade", "data_atualizacao"]
    search_fields = ["nome", "chave"]
