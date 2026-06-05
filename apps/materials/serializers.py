from rest_framework import serializers
from .models import Material, CategoriaMaterial, MovimentoEstoque


class CategoriaMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMaterial
        fields = ["id", "nome", "is_active"]


class MovimentoEstoqueSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source="usuario.nome", read_only=True)

    class Meta:
        model = MovimentoEstoque
        fields = [
            "id", "material", "tipo", "quantidade",
            "valor_unitario", "observacao", "usuario",
            "usuario_nome", "created_at",
        ]
        read_only_fields = ["id", "created_at", "usuario"]


class MaterialSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source="categoria.nome", read_only=True)
    quantidade_em_estoque = serializers.SerializerMethodField()
    estoque_critico = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = [
            "id", "codigo", "nome", "tipo", "categoria", "categoria_nome",
            "unidade_medida", "quantidade_estoque", "estoque_minimo",
            "valor_unitario", "quantidade_em_estoque", "estoque_critico",
            "observacoes", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_quantidade_em_estoque(self, obj):
        return obj.get_quantidade_em_estoque()

    def get_estoque_critico(self, obj):
        return obj.is_estoque_critico()
