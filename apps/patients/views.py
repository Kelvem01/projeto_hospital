from rest_framework import generics, permissions
from .models import Paciente, Convenio
from .serializers import PacienteSerializer, ConvenioSerializer


class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.filter(is_active=True)
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome", "cpf", "email"]
    ordering_fields = ["nome", "created_at"]


class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class ConvenioListCreateView(generics.ListCreateAPIView):
    queryset = Convenio.objects.filter(is_active=True)
    serializer_class = ConvenioSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome", "codigo"]


class ConvenioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer
    permission_classes = [permissions.IsAuthenticated]
