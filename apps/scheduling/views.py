from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cirurgia, ConsumoMaterialCirurgia
from .serializers import (
    CirurgiaListSerializer,
    CirurgiaCreateSerializer,
    CirurgiaDetailSerializer,
    ConsumoMaterialCirurgiaSerializer,
)


class CirurgiaListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["paciente__nome", "procedimento__nome"]
    filterset_fields = ["status", "data", "sala", "cirurgiao"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CirurgiaCreateSerializer
        return CirurgiaListSerializer

    def get_queryset(self):
        return Cirurgia.objects.select_related(
            "paciente", "procedimento", "sala", "cirurgiao"
        ).filter(is_active=True)


class CirurgiaDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return CirurgiaCreateSerializer
        return CirurgiaDetailSerializer

    def get_queryset(self):
        return Cirurgia.objects.select_related(
            "paciente", "procedimento", "sala", "cirurgiao"
        ).prefetch_related("materiais_consumidos__material")

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class ConsumoMaterialListCreateView(generics.ListCreateAPIView):
    queryset = ConsumoMaterialCirurgia.objects.select_related("material")
    serializer_class = ConsumoMaterialCirurgiaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["cirurgia", "is_extra"]
