from rest_framework import generics, permissions
from .models import Cirurgiao, Anestesista, Especialidade
from .serializers import CirurgiaoSerializer, AnestesistaSerializer, EspecialidadeSerializer


class CirurgiaoListCreateView(generics.ListCreateAPIView):
    queryset = Cirurgiao.objects.filter(is_active=True)
    serializer_class = CirurgiaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome", "cpf", "crm", "email"]
    ordering_fields = ["nome", "created_at"]


class CirurgiaoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cirurgiao.objects.all()
    serializer_class = CirurgiaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class AnestesistaListCreateView(generics.ListCreateAPIView):
    queryset = Anestesista.objects.filter(is_active=True)
    serializer_class = AnestesistaSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome", "cpf", "crm", "email"]
    ordering_fields = ["nome", "created_at"]


class AnestesistaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anestesista.objects.all()
    serializer_class = AnestesistaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class EspecialidadeListCreateView(generics.ListCreateAPIView):
    queryset = Especialidade.objects.filter(is_active=True)
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome", "codigo"]


class EspecialidadeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
