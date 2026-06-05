from django.contrib import admin
from .models import Cirurgia, ConsumoMaterialCirurgia


class ConsumoMaterialInline(admin.TabularInline):
    model = ConsumoMaterialCirurgia
    extra = 1


@admin.register(Cirurgia)
class CirurgiaAdmin(admin.ModelAdmin):
    list_display = [
        "paciente", "procedimento", "sala", "cirurgiao",
        "data", "hora_inicio", "status", "is_active",
    ]
    list_filter = ["status", "data", "sala"]
    search_fields = ["paciente__nome", "procedimento__nome"]
    inlines = [ConsumoMaterialInline]


@admin.register(ConsumoMaterialCirurgia)
class ConsumoMaterialCirurgiaAdmin(admin.ModelAdmin):
    list_display = ["cirurgia", "material", "quantidade", "is_extra"]
    list_filter = ["is_extra"]
