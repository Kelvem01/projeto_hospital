from django.db import models
from core.models import BasePersonModel


class Especialidade(models.Model):
    nome = models.CharField("nome", max_length=255, unique=True)
    codigo = models.CharField("código", max_length=20, unique=True)
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "especialidade"
        verbose_name_plural = "especialidades"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Cirurgiao(BasePersonModel):
    crm = models.CharField("CRM", max_length=20, unique=True)
    especialidades = models.ManyToManyField(
        Especialidade, verbose_name="especialidades",
        related_name="cirurgioes", blank=True
    )
    valor_hora = models.DecimalField(
        "valor por hora", max_digits=10, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = "cirurgião"
        verbose_name_plural = "cirurgiões"
        ordering = ["nome"]

    def __str__(self):
        return f"Dr. {self.nome} - CRM {self.crm}"


class Anestesista(BasePersonModel):
    crm = models.CharField("CRM", max_length=20, unique=True)
    valor_hora = models.DecimalField(
        "valor por hora", max_digits=10, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = "anestesista"
        verbose_name_plural = "anestesistas"
        ordering = ["nome"]

    def __str__(self):
        return f"Dr. {self.nome} - CRM {self.crm}"
