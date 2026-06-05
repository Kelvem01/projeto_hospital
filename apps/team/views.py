from rest_framework import generics, permissions
from .models import (
    ProfissionalEnfermagem, EquipeCirurgia,
    RegistroPresenca, TrocaPlantao,
)
from .serializers import (
    ProfissionalEnfermagemSerializer,
    EquipeCirurgiaSerializer,
    RegistroPresencaSerializer,
    TrocaPlantaoSerializer,
)


class ProfissionalEnfermagemListCreateView(generics.ListCreateAPIView):
    queryset = ProfissionalEnfermagem.objects.filter(is_active=True)
    serializer_class = ProfissionalEnfermagemSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome", "cpf", "coren"]
    filterset_fields = ["funcao"]


class ProfissionalEnfermagemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfissionalEnfermagem.objects.all()
    serializer_class = ProfissionalEnfermagemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class EquipeCirurgiaListCreateView(generics.ListCreateAPIView):
    queryset = EquipeCirurgia.objects.select_related(
        "cirurgia", "instrumentador", "anestesista", "circulante_atual"
    ).prefetch_related("presencas", "trocas_plantao")
    serializer_class = EquipeCirurgiaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquipeCirurgiaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipeCirurgia.objects.select_related(
        "cirurgia", "instrumentador", "anestesista", "circulante_atual"
    ).prefetch_related("presencas", "trocas_plantao")
    serializer_class = EquipeCirurgiaSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegistroPresencaListCreateView(generics.ListCreateAPIView):
    queryset = RegistroPresenca.objects.all()
    serializer_class = RegistroPresencaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["equipe"]


class TrocaPlantaoListCreateView(generics.ListCreateAPIView):
    queryset = TrocaPlantao.objects.all()
    serializer_class = TrocaPlantaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["equipe"]
