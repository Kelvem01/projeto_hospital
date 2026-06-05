from django.contrib import admin
from .models import Leito, Internacao, RegistroClinico, ConsumoInternacao


@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ["numero", "ala", "is_ocupado", "is_active"]
    list_filter = ["ala", "is_ocupado"]
    search_fields = ["numero", "ala"]


class RegistroClinicoInline(admin.TabularInline):
    model = RegistroClinico
    extra = 0
    readonly_fields = ["data_hora"]


class ConsumoInternacaoInline(admin.TabularInline):
    model = ConsumoInternacao
    extra = 1


@admin.register(Internacao)
class InternacaoAdmin(admin.ModelAdmin):
    list_display = ["paciente", "leito", "data_entrada", "data_alta", "is_active"]
    list_filter = ["data_alta"]
    search_fields = ["paciente__nome", "leito__numero"]
    inlines = [RegistroClinicoInline, ConsumoInternacaoInline]
