from django.db import models
from django.db.models import Sum, F
from core.models import BaseModel


class Faturamento(BaseModel):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("parcial", "Parcialmente Pago"),
        ("pago", "Pago"),
        ("cancelado", "Cancelado"),
    ]

    paciente = models.ForeignKey(
        "patients.Paciente", on_delete=models.PROTECT,
        verbose_name="paciente", related_name="faturamentos"
    )
    convenio = models.ForeignKey(
        "patients.Convenio", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="convênio"
    )
    data_emissao = models.DateTimeField("data de emissão", auto_now_add=True)
    status = models.CharField("status", max_length=20, choices=STATUS_CHOICES, default="pendente")
    observacoes = models.TextField("observações", blank=True, default="")

    class Meta:
        verbose_name = "faturamento"
        verbose_name_plural = "faturamentos"
        ordering = ["-data_emissao"]

    def __str__(self):
        return f"Faturamento #{self.id} - {self.paciente.nome} ({self.get_status_display()})"

    def calcular_valor_total(self):
        return (
            self.calcular_valor_sala()
            + self.calcular_valor_kits()
            + self.calcular_valor_materiais_extras()
            + self.calcular_valor_medicamentos()
            + self.calcular_valor_taxas()
        )

    def calcular_valor_sala(self):
        total = self.itens.filter(tipo="sala").aggregate(
            total=Sum(F("quantidade") * F("valor_unitario"))
        )["total"] or 0
        return float(total)

    def calcular_valor_kits(self):
        total = self.itens.filter(tipo="kit").aggregate(
            total=Sum(F("quantidade") * F("valor_unitario"))
        )["total"] or 0
        return float(total)

    def calcular_valor_materiais_extras(self):
        total = self.itens.filter(tipo="material_extra").aggregate(
            total=Sum(F("quantidade") * F("valor_unitario"))
        )["total"] or 0
        return float(total)

    def calcular_valor_medicamentos(self):
        total = self.itens.filter(tipo="medicamento").aggregate(
            total=Sum(F("quantidade") * F("valor_unitario"))
        )["total"] or 0
        return float(total)

    def calcular_valor_taxas(self):
        total = self.itens.filter(tipo="taxa").aggregate(
            total=Sum(F("quantidade") * F("valor_unitario"))
        )["total"] or 0
        return float(total)


class ItemFaturamento(BaseModel):
    TIPO_CHOICES = [
        ("sala", "Utilização de Sala"),
        ("kit", "Kit Cirúrgico"),
        ("material_extra", "Material Extra"),
        ("medicamento", "Medicamento"),
        ("taxa", "Taxa Hospitalar"),
        ("procedimento", "Procedimento"),
        ("outro", "Outro"),
    ]

    faturamento = models.ForeignKey(
        Faturamento, on_delete=models.CASCADE,
        verbose_name="faturamento", related_name="itens"
    )
    tipo = models.CharField("tipo", max_length=20, choices=TIPO_CHOICES)
    descricao = models.CharField("descrição", max_length=500)
    quantidade = models.DecimalField("quantidade", max_digits=10, decimal_places=2, default=1)
    valor_unitario = models.DecimalField("valor unitário", max_digits=10, decimal_places=2)
    cirurgia = models.ForeignKey(
        "scheduling.Cirurgia", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="cirurgia", related_name="itens_faturamento"
    )

    class Meta:
        verbose_name = "item do faturamento"
        verbose_name_plural = "itens do faturamento"
        ordering = ["tipo"]

    def __str__(self):
        return f"{self.get_tipo_display()}: {self.descricao} x{self.quantidade}"

    @property
    def valor_total(self):
        return float(self.quantidade) * float(self.valor_unitario)
