from rest_framework import generics, permissions
from .models import SalaCirurgica
from .serializers import SalaCirurgicaSerializer


class SalaCirurgicaListCreateView(generics.ListCreateAPIView):
    queryset = SalaCirurgica.objects.filter(is_active=True)
    serializer_class = SalaCirurgicaSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["numero", "nome"]
    ordering_fields = ["numero", "valor_hora"]


class SalaCirurgicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaCirurgica.objects.all()
    serializer_class = SalaCirurgicaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
