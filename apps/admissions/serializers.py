from rest_framework import serializers
from .models import Leito, Internacao, RegistroClinico, ConsumoInternacao


class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = ["id", "numero", "ala", "is_ocupado", "is_active", "created_at"]
        read_only_fields = ["id", "created_at"]


class RegistroClinicoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source="usuario.nome", read_only=True)

    class Meta:
        model = RegistroClinico
        fields = ["id", "internacao", "data_hora", "descricao", "usuario", "usuario_nome"]
        read_only_fields = ["id", "data_hora", "usuario"]


class ConsumoInternacaoSerializer(serializers.ModelSerializer):
    material_nome = serializers.CharField(source="material.nome", read_only=True)

    class Meta:
        model = ConsumoInternacao
        fields = [
            "id", "internacao", "material", "material_nome",
            "quantidade", "valor_unitario", "observacao", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class InternacaoSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    leito_numero = serializers.CharField(source="leito.numero", read_only=True)

    class Meta:
        model = Internacao
        fields = [
            "id", "paciente", "paciente_nome", "leito", "leito_numero",
            "data_entrada", "data_alta", "motivo", "observacoes",
            "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class InternacaoDetailSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    leito_numero = serializers.CharField(source="leito.numero", read_only=True)
    registros_clinicos = RegistroClinicoSerializer(many=True, read_only=True)
    consumos = ConsumoInternacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Internacao
        fields = [
            "id", "paciente", "paciente_nome", "leito", "leito_numero",
            "data_entrada", "data_alta", "motivo", "observacoes",
            "registros_clinicos", "consumos",
            "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
