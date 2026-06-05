from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db import transaction
from .models import Material, CategoriaMaterial, MovimentoEstoque
from .serializers import MaterialSerializer, CategoriaMaterialSerializer, MovimentoEstoqueSerializer


class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.filter(is_active=True)
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["codigo", "nome"]
    filterset_fields = ["tipo", "categoria"]


class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class CategoriaMaterialListCreateView(generics.ListCreateAPIView):
    queryset = CategoriaMaterial.objects.filter(is_active=True)
    serializer_class = CategoriaMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome"]


class CategoriaMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaMaterial.objects.all()
    serializer_class = CategoriaMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovimentoEstoqueListCreateView(generics.ListCreateAPIView):
    queryset = MovimentoEstoque.objects.all()
    serializer_class = MovimentoEstoqueSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["material", "tipo"]
    ordering_fields = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
