from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Leito, Internacao, RegistroClinico, ConsumoInternacao
from .serializers import (
    LeitoSerializer, InternacaoSerializer, InternacaoDetailSerializer,
    RegistroClinicoSerializer, ConsumoInternacaoSerializer,
)
from .filters.filters import InternacaoFilter   # ajuste o import se necessário


class LeitoListCreateView(generics.ListCreateAPIView):
    queryset = Leito.objects.filter(is_active=True)
    serializer_class = LeitoSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["numero", "ala"]
    filterset_fields = ["is_ocupado"]


class LeitoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [permissions.IsAuthenticated]


class InternacaoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["paciente__nome", "leito__numero"]
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = InternacaoFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return InternacaoSerializer
        return InternacaoDetailSerializer

    def get_queryset(self):
        return Internacao.objects.select_related(
            "paciente", "leito"
        ).prefetch_related("registros_clinicos", "consumos__material").filter(
            is_active=True
        )


class InternacaoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return InternacaoSerializer
        return InternacaoDetailSerializer

    def get_queryset(self):
        return Internacao.objects.select_related(
            "paciente", "leito"
        ).prefetch_related("registros_clinicos", "consumos__material")

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class RegistroClinicoListCreateView(generics.ListCreateAPIView):
    queryset = RegistroClinico.objects.all()
    serializer_class = RegistroClinicoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["internacao"]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ConsumoInternacaoListCreateView(generics.ListCreateAPIView):
    queryset = ConsumoInternacao.objects.all()
    serializer_class = ConsumoInternacaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["internacao"]