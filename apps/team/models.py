from django.db import models
from core.models import BaseModel, BasePersonModel


class ProfissionalEnfermagem(BasePersonModel):
    FUNCAO_CHOICES = [
        ("enfermeiro", "Enfermeiro"),
        ("tecnico", "Técnico de Enfermagem"),
        ("circulante", "Circulante"),
    ]

    coren = models.CharField("COREN", max_length=20, unique=True)
    funcao = models.CharField("função", max_length=20, choices=FUNCAO_CHOICES)

    class Meta:
        verbose_name = "profissional de enfermagem"
        verbose_name_plural = "profissionais de enfermagem"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.get_funcao_display()} (COREN {self.coren})"


class EquipeCirurgia(BaseModel):
    cirurgia = models.ForeignKey(
        "scheduling.Cirurgia", on_delete=models.CASCADE,
        verbose_name="cirurgia", related_name="equipe"
    )
    cirurgiao_auxiliar_1 = models.ForeignKey(
        "doctors.Cirurgiao", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="auxiliar 1",
        related_name="cirurgias_aux1"
    )
    cirurgiao_auxiliar_2 = models.ForeignKey(
        "doctors.Cirurgiao", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="auxiliar 2",
        related_name="cirurgias_aux2"
    )
    instrumentador = models.ForeignKey(
        ProfissionalEnfermagem, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="instrumentador",
        related_name="instrumentacoes"
    )
    anestesista = models.ForeignKey(
        "doctors.Anestesista", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="anestesista",
        related_name="cirurgias"
    )
    circulante_atual = models.ForeignKey(
        ProfissionalEnfermagem, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="circulante atual",
        related_name="circulacoes"
    )

    class Meta:
        verbose_name = "equipe da cirurgia"
        verbose_name_plural = "equipes das cirurgias"

    def __str__(self):
        return f"Equipe - {self.cirurgia}"


class RegistroPresenca(BaseModel):
    equipe = models.ForeignKey(
        EquipeCirurgia, on_delete=models.CASCADE,
        verbose_name="equipe", related_name="presencas"
    )
    profissional_nome = models.CharField("nome do profissional", max_length=255)
    funcao = models.CharField("função", max_length=50)
    entrada = models.DateTimeField("entrada")
    saida = models.DateTimeField("saída", null=True, blank=True)

    class Meta:
        verbose_name = "registro de presença"
        verbose_name_plural = "registros de presença"
        ordering = ["entrada"]

    @property
    def tempo_participacao(self):
        if self.saida:
            return (self.saida - self.entrada).total_seconds() / 3600
        return 0

    def __str__(self):
        return f"{self.profissional_nome} - {self.funcao} ({self.equipe.cirurgia})"


class TrocaPlantao(BaseModel):
    equipe = models.ForeignKey(
        EquipeCirurgia, on_delete=models.CASCADE,
        verbose_name="equipe", related_name="trocas_plantao"
    )
    circulante_saida = models.ForeignKey(
        ProfissionalEnfermagem, on_delete=models.SET_NULL,
        null=True, verbose_name="circulante que saiu",
        related_name="trocas_saida"
    )
    circulante_entrada = models.ForeignKey(
        ProfissionalEnfermagem, on_delete=models.SET_NULL,
        null=True, verbose_name="circulante que entrou",
        related_name="trocas_entrada"
    )
    data_hora_troca = models.DateTimeField("data/hora da troca")
    observacao = models.TextField("observação", blank=True, default="")

    class Meta:
        verbose_name = "troca de plantão"
        verbose_name_plural = "trocas de plantão"
        ordering = ["-data_hora_troca"]

    def __str__(self):
        return f"Troca: {self.circulante_saida} -> {self.circulante_entrada} em {self.data_hora_troca:%d/%m/%Y %H:%M}"
