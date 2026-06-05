from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["email", "nome", "nivel", "is_active"]
    list_filter = ["nivel", "is_active"]
    search_fields = ["email", "nome"]
    ordering = ["email"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações Pessoais", {"fields": ("nome", "telefone")}),
        ("Permissões", {"fields": ("nivel", "is_active", "is_staff", "is_superuser")}),
        ("Datas", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    readonly_fields = ["last_login", "created_at", "updated_at"]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nome", "password1", "password2", "nivel"),
        }),
    )
