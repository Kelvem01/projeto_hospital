from django.contrib import admin
from .models import KitCirurgico, KitItem


class KitItemInline(admin.TabularInline):
    model = KitItem
    extra = 1


@admin.register(KitCirurgico)
class KitCirurgicoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nome", "valor_total", "is_active"]
    search_fields = ["codigo", "nome"]
    inlines = [KitItemInline]


@admin.register(KitItem)
class KitItemAdmin(admin.ModelAdmin):
    list_display = ["kit", "material", "quantidade_padrao", "is_active"]
    list_filter = ["kit"]
    search_fields = ["kit__nome", "material__nome"]
