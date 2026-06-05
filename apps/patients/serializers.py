from rest_framework import serializers
from .models import Paciente, Convenio


class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = ["id", "nome", "codigo", "telefone", "is_active"]


class PacienteSerializer(serializers.ModelSerializer):
    convenio_nome = serializers.CharField(source="convenio.nome", read_only=True)

    class Meta:
        model = Paciente
        fields = [
            "id", "nome", "cpf", "rg", "email", "telefone",
            "profissao", "data_nascimento", "convenio", "convenio_nome",
            "numero_carteirinha", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
