from rest_framework import serializers
from .models import Cirurgiao, Anestesista, Especialidade


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ["id", "nome", "codigo", "is_active"]


class CirurgiaoSerializer(serializers.ModelSerializer):
    especialidades_nomes = serializers.SerializerMethodField()

    class Meta:
        model = Cirurgiao
        fields = [
            "id", "nome", "cpf", "crm", "email", "telefone",
            "especialidades", "especialidades_nomes",
            "valor_hora", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_especialidades_nomes(self, obj):
        return [e.nome for e in obj.especialidades.all()]


class AnestesistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anestesista
        fields = [
            "id", "nome", "cpf", "crm", "email", "telefone",
            "valor_hora", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
