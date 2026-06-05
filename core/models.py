from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class BasePersonModel(BaseModel):
    nome = models.CharField("nome", max_length=255)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    email = models.EmailField("e-mail", max_length=255, blank=True, default="")
    telefone = models.CharField("telefone", max_length=20, blank=True, default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome
