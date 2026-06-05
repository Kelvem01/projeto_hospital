from django.db import models


class SalaCirurgica(models.Model):
    STATUS_CHOICES = [
        ("disponivel", "Disponível"),
        ("ocupada", "Ocupada"),
        ("manutencao", "Em Manutenção"),
        ("reservada", "Reservada"),
    ]

    numero = models.CharField("número", max_length=10, unique=True)
    nome = models.CharField("nome", max_length=255, blank=True, default="")
    valor_hora = models.DecimalField("valor por hora", max_digits=10, decimal_places=2)
    status = models.CharField("status", max_length=20, choices=STATUS_CHOICES, default="disponivel")
    observacoes = models.TextField("observações", blank=True, default="")
    is_active = models.BooleanField("ativo", default=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "sala cirúrgica"
        verbose_name_plural = "salas cirúrgicas"
        ordering = ["numero"]

    def __str__(self):
        return f"Sala {self.numero} - {self.nome or self.get_status_display()}"
