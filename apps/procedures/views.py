from rest_framework import generics, permissions
from .models import Procedimento
from .serializers import ProcedimentoSerializer


class ProcedimentoListCreateView(generics.ListCreateAPIView):
    queryset = Procedimento.objects.filter(is_active=True)
    serializer_class = ProcedimentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["nome", "codigo_interno", "codigo_tuss"]
    filterset_fields = ["especialidade"]


class ProcedimentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
