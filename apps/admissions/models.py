from django.db import models
from core.models import BaseModel


class Leito(BaseModel):
    numero = models.CharField("número", max_length=10, unique=True)
    ala = models.CharField("ala", max_length=50, blank=True, default="")
    is_ocupado = models.BooleanField("ocupado", default=False)

    class Meta:
        verbose_name = "leito"
        verbose_name_plural = "leitos"
        ordering = ["ala", "numero"]

    def __str__(self):
        return f"Leito {self.numero} ({self.ala or 'Sem ala'})"


class Internacao(BaseModel):
    paciente = models.ForeignKey(
        "patients.Paciente", on_delete=models.PROTECT,
        verbose_name="paciente", related_name="internacoes"
    )
    leito = models.ForeignKey(
        Leito, on_delete=models.PROTECT,
        verbose_name="leito", related_name="internacoes"
    )
    data_entrada = models.DateTimeField("data de entrada")
    data_alta = models.DateTimeField("data de alta", null=True, blank=True)
    motivo = models.TextField("motivo", blank=True, default="")
    observacoes = models.TextField("observações", blank=True, default="")

    class Meta:
        verbose_name = "internação"
        verbose_name_plural = "internações"
        ordering = ["-data_entrada"]

    def __str__(self):
        return f"{self.paciente.nome} - Leito {self.leito.numero} ({self.data_entrada:%d/%m/%Y})"

    def save(self, *args, **kwargs):
        if not self.pk and self.leito:
            self.leito.is_ocupado = True
            self.leito.save()
        if self.data_alta and self.leito:
            self.leito.is_ocupado = False
            self.leito.save()
        super().save(*args, **kwargs)


class RegistroClinico(BaseModel):
    internacao = models.ForeignKey(
        Internacao, on_delete=models.CASCADE,
        verbose_name="internação", related_name="registros_clinicos"
    )
    data_hora = models.DateTimeField("data/hora", auto_now_add=True)
    descricao = models.TextField("descrição")
    usuario = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="usuário"
    )

    class Meta:
        verbose_name = "registro clínico"
        verbose_name_plural = "registros clínicos"
        ordering = ["-data_hora"]

    def __str__(self):
        return f"Registro - {self.internacao.paciente.nome} ({self.data_hora:%d/%m/%Y %H:%M})"


class ConsumoInternacao(BaseModel):
    internacao = models.ForeignKey(
        Internacao, on_delete=models.CASCADE,
        verbose_name="internação", related_name="consumos"
    )
    material = models.ForeignKey(
        "materials.Material", on_delete=models.PROTECT,
        verbose_name="material", related_name="consumos_internacao"
    )
    quantidade = models.DecimalField("quantidade", max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField("valor unitário", max_digits=10, decimal_places=2)
    observacao = models.TextField("observação", blank=True, default="")

    class Meta:
        verbose_name = "consumo da internação"
        verbose_name_plural = "consumos da internação"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.internacao} - {self.material.nome} x{self.quantidade}"
