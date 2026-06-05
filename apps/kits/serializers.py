from rest_framework import serializers
from .models import KitCirurgico, KitItem


class KitItemSerializer(serializers.ModelSerializer):
    material_nome = serializers.CharField(source="material.nome", read_only=True)
    material_codigo = serializers.CharField(source="material.codigo", read_only=True)

    class Meta:
        model = KitItem
        fields = [
            "id", "kit", "material", "material_nome", "material_codigo",
            "quantidade_padrao", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class KitCirurgicoSerializer(serializers.ModelSerializer):
    itens = KitItemSerializer(many=True, read_only=True)
    valor_calculado = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True, source="valor_total"
    )

    class Meta:
        model = KitCirurgico
        fields = [
            "id", "codigo", "nome", "descricao",
            "valor_total", "valor_calculado", "itens",
            "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
