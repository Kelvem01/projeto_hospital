from django.contrib import admin
from .models import Faturamento, ItemFaturamento


class ItemFaturamentoInline(admin.TabularInline):
    model = ItemFaturamento
    extra = 1


@admin.register(Faturamento)
class FaturamentoAdmin(admin.ModelAdmin):
    list_display = ["id", "paciente", "convenio", "data_emissao", "status", "is_active"]
    list_filter = ["status", "data_emissao"]
    search_fields = ["paciente__nome"]
    inlines = [ItemFaturamentoInline]


@admin.register(ItemFaturamento)
class ItemFaturamentoAdmin(admin.ModelAdmin):
    list_display = ["faturamento", "tipo", "descricao", "quantidade", "valor_unitario"]
    list_filter = ["tipo"]
    search_fields = ["descricao"]
