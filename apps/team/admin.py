from django.contrib import admin
from .models import ProfissionalEnfermagem, EquipeCirurgia, RegistroPresenca, TrocaPlantao


@admin.register(ProfissionalEnfermagem)
class ProfissionalEnfermagemAdmin(admin.ModelAdmin):
    list_display = ["nome", "coren", "funcao", "email", "is_active"]
    list_filter = ["funcao", "is_active"]
    search_fields = ["nome", "coren", "cpf"]


class RegistroPresencaInline(admin.TabularInline):
    model = RegistroPresenca
    extra = 1


class TrocaPlantaoInline(admin.TabularInline):
    model = TrocaPlantao
    extra = 0


@admin.register(EquipeCirurgia)
class EquipeCirurgiaAdmin(admin.ModelAdmin):
    list_display = ["cirurgia", "instrumentador", "anestesista", "circulante_atual"]
    inlines = [RegistroPresencaInline, TrocaPlantaoInline]


@admin.register(TrocaPlantao)
class TrocaPlantaoAdmin(admin.ModelAdmin):
    list_display = ["equipe", "circulante_saida", "circulante_entrada", "data_hora_troca"]
    list_filter = ["data_hora_troca"]
