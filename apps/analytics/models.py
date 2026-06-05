from django.db import models
from core.models import BaseModel


class InsightIA(BaseModel):
    TIPO_CHOICES = [
        ("ocupacao", "Análise de Ocupação"),
        ("financeiro", "Análise Financeira"),
        ("estoque", "Análise de Estoque"),
        ("gerencial", "Relatório Gerencial"),
    ]

    tipo = models.CharField("tipo", max_length=20, choices=TIPO_CHOICES)
    titulo = models.CharField("título", max_length=255)
    descricao = models.TextField("descrição")
    dados_json = models.JSONField("dados", null=True, blank=True)
    data_referencia = models.DateField("data de referência")
    gerado_por = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="gerado por"
    )

    class Meta:
        verbose_name = "insight de IA"
        verbose_name_plural = "insights de IA"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_tipo_display()}: {self.titulo} ({self.data_referencia})"


class Dashboard(BaseModel):
    nome = models.CharField("nome", max_length=255)
    tipo = models.CharField("tipo", max_length=50)
    config_json = models.JSONField("configuração")
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "dashboard"
        verbose_name_plural = "dashboards"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Indicador(BaseModel):
    nome = models.CharField("nome", max_length=255)
    chave = models.CharField("chave", max_length=50, unique=True)
    descricao = models.TextField("descrição", blank=True, default="")
    valor_atual = models.DecimalField("valor atual", max_digits=15, decimal_places=2, default=0)
    valor_anterior = models.DecimalField(
        "valor anterior", max_digits=15, decimal_places=2, default=0
    )
    unidade = models.CharField("unidade", max_length=20, default="")
    data_atualizacao = models.DateTimeField("data de atualização", auto_now=True)

    class Meta:
        verbose_name = "indicador"
        verbose_name_plural = "indicadores"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome}: {self.valor_atual} {self.unidade}"

    @property
    def variacao_percentual(self):
        if float(self.valor_anterior) == 0:
            return 0
        return ((float(self.valor_atual) - float(self.valor_anterior)) / float(self.valor_anterior)) * 100
