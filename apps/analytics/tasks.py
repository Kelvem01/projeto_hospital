from celery import shared_task
from django.utils import timezone
from .services import AIService, DashboardService


@shared_task
def atualizar_indicadores():
    service = DashboardService()
    stats = service.get_centro_cirurgico_stats()

    from .models import Indicador
    indicador, _ = Indicador.objects.get_or_create(
        chave="taxa_ocupacao",
        defaults={"nome": "Taxa de Ocupação", "unidade": "%"},
    )
    indicador.valor_anterior = indicador.valor_atual
    indicador.valor_atual = stats["taxa_ocupacao"]
    indicador.save()


@shared_task
def gerar_insights_periodicos():
    ai = AIService()
    if not ai.is_available():
        return "IA not available"

    analise = ai.gerar_analise_ocupacao()
    from .models import InsightIA
    InsightIA.objects.create(
        tipo="ocupacao",
        titulo="Análise Automática de Ocupação",
        descricao=analise,
        data_referencia=timezone.now().date(),
    )
    return "Insight generated"
