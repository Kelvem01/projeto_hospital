from django.db import models
from django.utils import timezone
from core.models import BaseModel
from core.exceptions import ConflictException, BusinessRuleException


class Cirurgia(BaseModel):
    STATUS_CHOICES = [
        ("agendada", "Agendada"),
        ("em_andamento", "Em Andamento"),
        ("realizada", "Realizada"),
        ("cancelada", "Cancelada"),
        ("suspensa", "Suspensa"),
    ]

    paciente = models.ForeignKey(
        "patients.Paciente", on_delete=models.PROTECT,
        verbose_name="paciente", related_name="cirurgias"
    )
    procedimento = models.ForeignKey(
        "procedures.Procedimento", on_delete=models.PROTECT,
        verbose_name="procedimento", related_name="cirurgias"
    )
    sala = models.ForeignKey(
        "rooms.SalaCirurgica", on_delete=models.PROTECT,
        verbose_name="sala", related_name="cirurgias"
    )
    cirurgiao = models.ForeignKey(
        "doctors.Cirurgiao", on_delete=models.PROTECT,
        verbose_name="cirurgião principal", related_name="cirurgias"
    )
    data = models.DateField("data da cirurgia")
    hora_inicio = models.TimeField("hora de início")
    hora_prevista_termino = models.TimeField("hora prevista de término")
    hora_inicio_real = models.TimeField("hora de início real", null=True, blank=True)
    hora_termino_real = models.TimeField("hora de término real", null=True, blank=True)
    status = models.CharField("status", max_length=20, choices=STATUS_CHOICES, default="agendada")
    observacoes = models.TextField("observações", blank=True, default="")
    convenio = models.ForeignKey(
        "patients.Convenio", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="convênio"
    )

    class Meta:
        verbose_name = "cirurgia"
        verbose_name_plural = "cirurgias"
        ordering = ["-data", "hora_inicio"]

    def __str__(self):
        return f"{self.paciente.nome} - {self.procedimento.nome} ({self.data})"

    def clean(self):
        if self.hora_inicio and self.hora_prevista_termino:
            if self.hora_prevista_termino <= self.hora_inicio:
                raise BusinessRuleException(
                    "Horário de término deve ser posterior ao horário de início"
                )

    def verificar_conflito_sala(self):
        conflitos = Cirurgia.objects.filter(
            sala=self.sala,
            data=self.data,
            status__in=["agendada", "em_andamento"],
        ).exclude(pk=self.pk)

        for c in conflitos:
            if (
                self.hora_inicio < c.hora_prevista_termino
                and self.hora_prevista_termino > c.hora_inicio
            ):
                raise ConflictException(
                    f"Conflito de horário na {self.sala} com "
                    f"'{c.paciente.nome}' das {c.hora_inicio} às {c.hora_prevista_termino}"
                )

    def verificar_disponibilidade_cirurgiao(self):
        conflitos = Cirurgia.objects.filter(
            cirurgiao=self.cirurgiao,
            data=self.data,
            status__in=["agendada", "em_andamento"],
        ).exclude(pk=self.pk)

        for c in conflitos:
            if (
                self.hora_inicio < c.hora_prevista_termino
                and self.hora_prevista_termino > c.hora_inicio
            ):
                raise ConflictException(
                    f"Cirurgião já possui cirurgia agendada neste horário: "
                    f"'{c.paciente.nome}' das {c.hora_inicio} às {c.hora_prevista_termino}"
                )

    def calcular_tempo_total(self):
        if self.hora_inicio_real and self.hora_termino_real:
            inicio = timezone.datetime.combine(self.data, self.hora_inicio_real)
            termino = timezone.datetime.combine(self.data, self.hora_termino_real)
            if termino < inicio:
                termino = timezone.datetime.combine(
                    self.data + timezone.timedelta(days=1), self.hora_termino_real
                )
            return (termino - inicio).total_seconds() / 3600
        return 0

    def save(self, *args, **kwargs):
        self.clean()
        if self.status in ("agendada",) and not self.pk:
            self.verificar_conflito_sala()
            self.verificar_disponibilidade_cirurgiao()
        super().save(*args, **kwargs)


class ConsumoMaterialCirurgia(BaseModel):
    cirurgia = models.ForeignKey(
        Cirurgia, on_delete=models.CASCADE,
        verbose_name="cirurgia", related_name="materiais_consumidos"
    )
    material = models.ForeignKey(
        "materials.Material", on_delete=models.PROTECT,
        verbose_name="material", related_name="consumos_cirurgia"
    )
    quantidade = models.DecimalField("quantidade", max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField("valor unitário", max_digits=10, decimal_places=2)
    is_extra = models.BooleanField("material extra", default=False)
    observacao = models.TextField("observação", blank=True, default="")

    class Meta:
        verbose_name = "consumo de material em cirurgia"
        verbose_name_plural = "consumos de materiais em cirurgias"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.cirurgia} - {self.material.nome} x{self.quantidade}"
