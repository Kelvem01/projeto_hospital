from rest_framework import serializers
from .models import InsightIA, Dashboard, Indicador


class InsightIASerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightIA
        fields = [
            "id", "tipo", "titulo", "descricao",
            "dados_json", "data_referencia", "gerado_por",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ["id", "nome", "tipo", "config_json", "is_active"]


class IndicadorSerializer(serializers.ModelSerializer):
    variacao_percentual = serializers.ReadOnlyField()

    class Meta:
        model = Indicador
        fields = [
            "id", "nome", "chave", "descricao",
            "valor_atual", "valor_anterior", "variacao_percentual",
            "unidade", "data_atualizacao",
        ]
