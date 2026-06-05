from django.db import models
from core.models import BaseModel
from apps.doctors.models import Especialidade


class Procedimento(BaseModel):
    nome = models.CharField("nome", max_length=255)
    codigo_interno = models.CharField("código interno", max_length=20, unique=True)
    codigo_tuss = models.CharField("código TUSS", max_length=20, blank=True, default="")
    tempo_medio_previsto = models.DurationField("tempo médio previsto", null=True, blank=True)
    valor_base = models.DecimalField("valor base", max_digits=10, decimal_places=2, default=0)
    especialidade = models.ForeignKey(
        Especialidade, on_delete=models.PROTECT,
        verbose_name="especialidade", related_name="procedimentos",
        null=True, blank=True
    )
    observacoes = models.TextField("observações", blank=True, default="")

    class Meta:
        verbose_name = "procedimento"
        verbose_name_plural = "procedimentos"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.codigo_interno} - {self.nome}"
