from django.db import models
from core.models import BasePersonModel


class Convenio(models.Model):
    nome = models.CharField("nome", max_length=255, unique=True)
    codigo = models.CharField("código", max_length=20, unique=True)
    telefone = models.CharField("telefone", max_length=20, blank=True, default="")
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "convênio"
        verbose_name_plural = "convênios"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Paciente(BasePersonModel):
    rg = models.CharField("RG", max_length=20, blank=True, default="")
    profissao = models.CharField("profissão", max_length=255, blank=True, default="")
    data_nascimento = models.DateField("data de nascimento", null=True, blank=True)
    convenio = models.ForeignKey(
        Convenio, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="convênio", related_name="pacientes"
    )
    numero_carteirinha = models.CharField("carteirinha", max_length=50, blank=True, default="")

    class Meta:
        verbose_name = "paciente"
        verbose_name_plural = "pacientes"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.cpf}"
