from django.db import models
from core.models import BaseModel
from apps.materials.models import Material


class KitCirurgico(BaseModel):
    codigo = models.CharField("código", max_length=20, unique=True)
    nome = models.CharField("nome", max_length=255)
    descricao = models.TextField("descrição", blank=True, default="")
    valor_total = models.DecimalField(
        "valor total", max_digits=10, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = "kit cirúrgico"
        verbose_name_plural = "kits cirúrgicos"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

    def calcular_valor_total(self):
        total = sum(
            item.quantidade_padrao * float(item.material.valor_unitario)
            for item in self.itens.select_related("material").all()
            if item.material
        )
        self.valor_total = total
        self.save(update_fields=["valor_total"])
        return total


class KitItem(BaseModel):
    kit = models.ForeignKey(
        KitCirurgico, on_delete=models.CASCADE,
        verbose_name="kit", related_name="itens"
    )
    material = models.ForeignKey(
        Material, on_delete=models.PROTECT,
        verbose_name="material", related_name="kits"
    )
    quantidade_padrao = models.DecimalField(
        "quantidade padrão", max_digits=10, decimal_places=2, default=1
    )

    class Meta:
        verbose_name = "item do kit"
        verbose_name_plural = "itens dos kits"
        unique_together = ["kit", "material"]
        ordering = ["kit", "material"]

    def __str__(self):
        return f"{self.kit.nome} - {self.material.nome} ({self.quantidade_padrao})"
