from rest_framework import serializers
from .models import SalaCirurgica


class SalaCirurgicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaCirurgica
        fields = [
            "id", "numero", "nome", "valor_hora", "status",
            "observacoes", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
