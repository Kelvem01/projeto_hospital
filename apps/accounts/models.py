from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("nivel", "administrador")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    NIVEL_CHOICES = [
        ("administrador", "Administrador"),
        ("medico", "Médico"),
        ("enfermeiro", "Enfermeiro"),
        ("financeiro", "Financeiro"),
        ("estoque", "Estoque"),
    ]

    email = models.EmailField("e-mail", max_length=255, unique=True)
    nome = models.CharField("nome", max_length=255)
    telefone = models.CharField("telefone", max_length=20, blank=True, default="")
    nivel = models.CharField("nível", max_length=20, choices=NIVEL_CHOICES, default="medico")
    is_active = models.BooleanField("ativo", default=True)
    is_staff = models.BooleanField("equipe", default=False)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} ({self.get_nivel_display()})"
