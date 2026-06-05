from django.db import models
from core.models import BaseModel


class CategoriaMaterial(models.Model):
    nome = models.CharField("nome", max_length=255, unique=True)
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "categoria de material"
        verbose_name_plural = "categorias de materiais"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Material(BaseModel):
    TIPO_CHOICES = [
        ("material", "Material Hospitalar"),
        ("medicamento", "Medicamento"),
        ("opme", "OPME"),
        ("insumo", "Insumo"),
    ]

    codigo = models.CharField("código", max_length=50, unique=True)
    nome = models.CharField("nome", max_length=255)
    tipo = models.CharField("tipo", max_length=20, choices=TIPO_CHOICES)
    categoria = models.ForeignKey(
        CategoriaMaterial, on_delete=models.PROTECT,
        verbose_name="categoria", related_name="materiais",
        null=True, blank=True
    )
    unidade_medida = models.CharField("unidade de medida", max_length=20, default="un")
    quantidade_estoque = models.DecimalField(
        "quantidade em estoque", max_digits=10, decimal_places=2, default=0
    )
    estoque_minimo = models.DecimalField(
        "estoque mínimo", max_digits=10, decimal_places=2, default=0
    )
    valor_unitario = models.DecimalField(
        "valor unitário", max_digits=10, decimal_places=2, default=0
    )
    observacoes = models.TextField("observações", blank=True, default="")

    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materiais"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.get_quantidade_em_estoque():.0f} {self.unidade_medida})"

    def get_quantidade_em_estoque(self) -> float:
        entradas = self.movimentos.filter(tipo="entrada").aggregate(
            total=models.Sum("quantidade"))["total"] or 0
        saidas = self.movimentos.filter(tipo="saida").aggregate(
            total=models.Sum("quantidade"))["total"] or 0
        return float(entradas - saidas)

    def is_estoque_critico(self) -> bool:
        return self.get_quantidade_em_estoque() <= float(self.estoque_minimo)


class MovimentoEstoque(BaseModel):
    TIPO_CHOICES = [
        ("entrada", "Entrada"),
        ("saida", "Saída"),
        ("ajuste", "Ajuste"),
    ]

    material = models.ForeignKey(
        Material, on_delete=models.CASCADE,
        verbose_name="material", related_name="movimentos"
    )
    tipo = models.CharField("tipo", max_length=10, choices=TIPO_CHOICES)
    quantidade = models.DecimalField("quantidade", max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(
        "valor unitário", max_digits=10, decimal_places=2, default=0
    )
    observacao = models.TextField("observação", blank=True, default="")
    usuario = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="usuário"
    )

    class Meta:
        verbose_name = "movimento de estoque"
        verbose_name_plural = "movimentos de estoque"
        ordering = ["-created_at"]
