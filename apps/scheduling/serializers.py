from rest_framework import serializers
from .models import Cirurgia, ConsumoMaterialCirurgia


class ConsumoMaterialCirurgiaSerializer(serializers.ModelSerializer):
    material_nome = serializers.CharField(source="material.nome", read_only=True)
    material_codigo = serializers.CharField(source="material.codigo", read_only=True)

    class Meta:
        model = ConsumoMaterialCirurgia
        fields = [
            "id", "cirurgia", "material", "material_nome", "material_codigo",
            "quantidade", "valor_unitario", "is_extra", "observacao", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class CirurgiaListSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    procedimento_nome = serializers.CharField(source="procedimento.nome", read_only=True)
    sala_nome = serializers.CharField(source="sala.nome", read_only=True)
    sala_numero = serializers.CharField(source="sala.numero", read_only=True)
    cirurgiao_nome = serializers.CharField(source="cirurgiao.nome", read_only=True)

    class Meta:
        model = Cirurgia
        fields = [
            "id", "paciente", "paciente_nome", "procedimento", "procedimento_nome",
            "sala", "sala_nome", "sala_numero", "cirurgiao", "cirurgiao_nome",
            "data", "hora_inicio", "hora_prevista_termino",
            "hora_inicio_real", "hora_termino_real",
            "status", "observacoes", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class CirurgiaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cirurgia
        fields = [
            "paciente", "procedimento", "sala", "cirurgiao",
            "data", "hora_inicio", "hora_prevista_termino",
            "convenio", "observacoes",
        ]


class CirurgiaDetailSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    paciente_cpf = serializers.CharField(source="paciente.cpf", read_only=True)
    procedimento_nome = serializers.CharField(source="procedimento.nome", read_only=True)
    procedimento_codigo = serializers.CharField(source="procedimento.codigo_interno", read_only=True)
    sala_nome = serializers.CharField(source="sala.nome", read_only=True)
    sala_numero = serializers.CharField(source="sala.numero", read_only=True)
    sala_valor_hora = serializers.DecimalField(source="sala.valor_hora", max_digits=10, decimal_places=2, read_only=True)
    cirurgiao_nome = serializers.CharField(source="cirurgiao.nome", read_only=True)
    materiais_consumidos = ConsumoMaterialCirurgiaSerializer(many=True, read_only=True)
    tempo_total_horas = serializers.SerializerMethodField()

    class Meta:
        model = Cirurgia
        fields = [
            "id", "paciente", "paciente_nome", "paciente_cpf",
            "procedimento", "procedimento_nome", "procedimento_codigo",
            "sala", "sala_nome", "sala_numero", "sala_valor_hora",
            "cirurgiao", "cirurgiao_nome",
            "data", "hora_inicio", "hora_prevista_termino",
            "hora_inicio_real", "hora_termino_real",
            "tempo_total_horas", "status", "convenio", "observacoes",
            "materiais_consumidos", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_tempo_total_horas(self, obj):
        return obj.calcular_tempo_total()
