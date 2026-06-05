from rest_framework import serializers
from .models import (
    ProfissionalEnfermagem, EquipeCirurgia,
    RegistroPresenca, TrocaPlantao,
)


class ProfissionalEnfermagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalEnfermagem
        fields = [
            "id", "nome", "cpf", "coren", "email", "telefone",
            "funcao", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class RegistroPresencaSerializer(serializers.ModelSerializer):
    tempo_participacao = serializers.ReadOnlyField()

    class Meta:
        model = RegistroPresenca
        fields = [
            "id", "equipe", "profissional_nome", "funcao",
            "entrada", "saida", "tempo_participacao", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class TrocaPlantaoSerializer(serializers.ModelSerializer):
    circulante_saida_nome = serializers.CharField(
        source="circulante_saida.nome", read_only=True
    )
    circulante_entrada_nome = serializers.CharField(
        source="circulante_entrada.nome", read_only=True
    )

    class Meta:
        model = TrocaPlantao
        fields = [
            "id", "equipe", "circulante_saida", "circulante_saida_nome",
            "circulante_entrada", "circulante_entrada_nome",
            "data_hora_troca", "observacao", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class EquipeCirurgiaSerializer(serializers.ModelSerializer):
    presencas = RegistroPresencaSerializer(many=True, read_only=True)
    trocas_plantao = TrocaPlantaoSerializer(many=True, read_only=True)

    class Meta:
        model = EquipeCirurgia
        fields = [
            "id", "cirurgia", "cirurgiao_auxiliar_1", "cirurgiao_auxiliar_2",
            "instrumentador", "anestesista", "circulante_atual",
            "presencas", "trocas_plantao", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
