import json
from datetime import date, timedelta
from django.db.models import Count, Sum, F, Avg, Q
from django.utils import timezone
from apps.scheduling.models import Cirurgia
from apps.rooms.models import SalaCirurgica
from apps.billing.models import Faturamento
from apps.materials.models import Material, MovimentoEstoque

try:
    from langchain_openai import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    from langchain.schema import SystemMessage, HumanMessage
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False


class DashboardService:
    def get_centro_cirurgico_stats(self):
        salas = SalaCirurgica.objects.filter(is_active=True)
        total_salas = salas.count()
        ocupadas = salas.filter(status="ocupada").count()
        disponiveis = salas.filter(status="disponivel").count()
        manutencao = salas.filter(status="manutencao").count()

        hoje = date.today()
        cirurgias_hoje = Cirurgia.objects.filter(
            data=hoje, is_active=True, status__in=["agendada", "em_andamento"]
        ).count()

        tempo_medio = Cirurgia.objects.filter(
            status="realizada",
            hora_inicio_real__isnull=False,
            hora_termino_real__isnull=False,
        ).aggregate(
            tempo_medio=Avg(
                F("hora_termino_real") - F("hora_inicio_real")
            )
        )["tempo_medio"]

        return {
            "total_salas": total_salas,
            "salas_ocupadas": ocupadas,
            "salas_disponiveis": disponiveis,
            "salas_manutencao": manutencao,
            "taxa_ocupacao": round((ocupadas / total_salas * 100) if total_salas else 0, 1),
            "cirurgias_hoje": cirurgias_hoje,
            "tempo_medio_cirurgico": str(tempo_medio) if tempo_medio else "N/A",
        }

    def get_financeiro_stats(self):
        mes_atual = date.today().replace(day=1)
        receita_mensal = Faturamento.objects.filter(
            data_emissao__gte=mes_atual,
            status__in=["pago", "parcial"],
            is_active=True,
        ).aggregate(total=Sum("itens__quantidade__sum")) or {"total": 0}

        return {
            "receita_mensal": receita_mensal.get("total") or 0,
        }

    def get_estoque_stats(self):
        materiais_criticos = Material.objects.filter(is_active=True)
        criticos = []
        for m in materiais_criticos:
            if m.is_estoque_critico():
                criticos.append({
                    "id": m.id,
                    "nome": m.nome,
                    "codigo": m.codigo,
                    "quantidade": m.get_quantidade_em_estoque(),
                    "estoque_minimo": float(m.estoque_minimo),
                })

        mais_consumidos = MovimentoEstoque.objects.filter(
            tipo="saida",
            created_at__gte=timezone.now() - timedelta(days=30),
        ).values("material__nome", "material__codigo").annotate(
            total=Sum("quantidade")
        ).order_by("-total")[:10]

        return {
            "materiais_criticos": criticos,
            "total_criticos": len(criticos),
            "mais_consumidos": list(mais_consumidos),
        }


class AIService:
    def __init__(self):
        self.llm = None
        if LANGCHAIN_AVAILABLE:
            from django.conf import settings
            if settings.OPENAI_API_KEY:
                self.llm = ChatOpenAI(
                    model=settings.LANGCHAIN_MODEL,
                    temperature=0.3,
                    api_key=settings.OPENAI_API_KEY,
                )

    def is_available(self):
        return self.llm is not None

    def gerar_analise_ocupacao(self):
        stats = DashboardService().get_centro_cirurgico_stats()
        if not self.is_available():
            return self._fallback_analise_ocupacao(stats)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um analista hospitalar especializado em centro cirúrgico."),
            ("human", (
                "Analise os seguintes dados de ocupação do centro cirúrgico e "
                "gere insights sobre:\n"
                "1. Horários ociosos e salas subutilizadas\n"
                "2. Gargalos operacionais\n"
                "3. Recomendações de melhoria\n\n"
                f"Dados: {json.dumps(stats, indent=2)}"
            )),
        ])

        response = self.llm.invoke(prompt.format_messages())
        return response.content

    def _fallback_analise_ocupacao(self, stats):
        taxa = stats["taxa_ocupacao"]
        if taxa < 50:
            return (
                f"ALERTA: Taxa de ocupação baixa ({taxa}%). "
                "Salas subutilizadas. Recomenda-se revisar agendamentos."
            )
        elif taxa > 90:
                return (
                    f"ALERTA: Taxa de ocupação crítica ({taxa}%). "
                    "Risco de gargalos operacionais."
                )
        return (
            f"Taxa de ocupação saudável ({taxa}%). "
            "Operação dentro do esperado."
        )

    def gerar_analise_financeira(self):
        from django.db.models.functions import TruncMonth
        from apps.billing.models import ItemFaturamento

        fat_por_procedimento = ItemFaturamento.objects.filter(
            tipo__in=["sala", "kit", "material_extra", "procedimento"],
            faturamento__status__in=["pago", "parcial"],
        ).values("descricao").annotate(
            total_receita=Sum(F("quantidade") * F("valor_unitario")),
            total_custo=Sum("valor_unitario"),
            quantidade=Count("id"),
        ).order_by("-total_receita")[:10]

        return {
            "procedimentos_mais_lucrativos": [
                p for p in fat_por_procedimento if p["total_receita"] > 0
            ],
        }

    def gerar_relatorio_gerencial(self):
        dados = {
            "centro_cirurgico": DashboardService().get_centro_cirurgico_stats(),
            "estoque": DashboardService().get_estoque_stats(),
        }

        if not self.is_available():
            return "Relatório gerencial baseado em dados estáticos do sistema."

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um diretor hospitalar gerando relatórios executivos."),
            ("human", (
                "Gere um resumo executivo conciso com base nos dados:\n\n"
                f"{json.dumps(dados, indent=2)}"
            )),
        ])

        response = self.llm.invoke(prompt.format_messages())
        return response.content
