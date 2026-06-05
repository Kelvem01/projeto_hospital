from rest_framework import serializers
from .models import Procedimento


class ProcedimentoSerializer(serializers.ModelSerializer):
    especialidade_nome = serializers.CharField(source="especialidade.nome", read_only=True)

    class Meta:
        model = Procedimento
        fields = [
            "id", "nome", "codigo_interno", "codigo_tuss",
            "tempo_medio_previsto", "valor_base",
            "especialidade", "especialidade_nome",
            "observacoes", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
