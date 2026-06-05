from django.contrib import admin
from .models import SalaCirurgica


@admin.register(SalaCirurgica)
class SalaCirurgicaAdmin(admin.ModelAdmin):
    list_display = ["numero", "nome", "valor_hora", "status", "is_active"]
    list_filter = ["status", "is_active"]
    search_fields = ["numero", "nome"]
