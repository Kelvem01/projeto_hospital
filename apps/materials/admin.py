from django.contrib import admin
from .models import Material, CategoriaMaterial, MovimentoEstoque


@admin.register(CategoriaMaterial)
class CategoriaMaterialAdmin(admin.ModelAdmin):
    list_display = ["nome", "is_active"]
    search_fields = ["nome"]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nome", "tipo", "categoria", "valor_unitario", "is_active"]
    list_filter = ["tipo", "categoria", "is_active"]
    search_fields = ["codigo", "nome"]


@admin.register(MovimentoEstoque)
class MovimentoEstoqueAdmin(admin.ModelAdmin):
    list_display = ["material", "tipo", "quantidade", "created_at", "usuario"]
    list_filter = ["tipo", "created_at"]
    search_fields = ["material__nome", "material__codigo"]
