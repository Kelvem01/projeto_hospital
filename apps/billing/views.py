from rest_framework import generics, permissions
from .models import Faturamento, ItemFaturamento
from .serializers import (
    FaturamentoListSerializer,
    FaturamentoDetailSerializer,
    ItemFaturamentoSerializer,
)


class FaturamentoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["paciente__nome"]
    filterset_fields = ["status", "data_emissao"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return FaturamentoListSerializer
        return FaturamentoListSerializer

    def get_queryset(self):
        return Faturamento.objects.select_related(
            "paciente", "convenio"
        ).filter(is_active=True)


class FaturamentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return FaturamentoListSerializer
        return FaturamentoDetailSerializer

    def get_queryset(self):
        return Faturamento.objects.select_related(
            "paciente", "convenio"
        ).prefetch_related("itens")

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class ItemFaturamentoListCreateView(generics.ListCreateAPIView):
    queryset = ItemFaturamento.objects.all()
    serializer_class = ItemFaturamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["faturamento", "tipo"]


class ItemFaturamentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemFaturamento.objects.all()
    serializer_class = ItemFaturamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
