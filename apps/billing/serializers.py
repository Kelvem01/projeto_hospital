from rest_framework import serializers
from .models import Faturamento, ItemFaturamento


class ItemFaturamentoSerializer(serializers.ModelSerializer):
    valor_total = serializers.ReadOnlyField()

    class Meta:
        model = ItemFaturamento
        fields = [
            "id", "faturamento", "tipo", "descricao",
            "quantidade", "valor_unitario", "valor_total",
            "cirurgia", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class FaturamentoListSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    convenio_nome = serializers.CharField(source="convenio.nome", read_only=True)
    valor_total = serializers.SerializerMethodField()

    class Meta:
        model = Faturamento
        fields = [
            "id", "paciente", "paciente_nome", "convenio", "convenio_nome",
            "data_emissao", "status", "valor_total", "observacoes",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "data_emissao", "created_at", "updated_at"]

    def get_valor_total(self, obj):
        return obj.calcular_valor_total()


class FaturamentoDetailSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    convenio_nome = serializers.CharField(source="convenio.nome", read_only=True)
    itens = ItemFaturamentoSerializer(many=True, read_only=True)
    valor_total = serializers.SerializerMethodField()
    valor_sala = serializers.SerializerMethodField()
    valor_kits = serializers.SerializerMethodField()
    valor_materiais_extras = serializers.SerializerMethodField()
    valor_medicamentos = serializers.SerializerMethodField()
    valor_taxas = serializers.SerializerMethodField()

    class Meta:
        model = Faturamento
        fields = [
            "id", "paciente", "paciente_nome", "convenio", "convenio_nome",
            "data_emissao", "status", "observacoes",
            "valor_total", "valor_sala", "valor_kits",
            "valor_materiais_extras", "valor_medicamentos", "valor_taxas",
            "itens", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "data_emissao", "created_at", "updated_at"]

    def get_valor_total(self, obj): return obj.calcular_valor_total()
    def get_valor_sala(self, obj): return obj.calcular_valor_sala()
    def get_valor_kits(self, obj): return obj.calcular_valor_kits()
    def get_valor_materiais_extras(self, obj): return obj.calcular_valor_materiais_extras()
    def get_valor_medicamentos(self, obj): return obj.calcular_valor_medicamentos()
    def get_valor_taxas(self, obj): return obj.calcular_valor_taxas()
