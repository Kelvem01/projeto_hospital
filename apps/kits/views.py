from rest_framework import generics, permissions
from .models import KitCirurgico, KitItem
from .serializers import KitCirurgicoSerializer, KitItemSerializer


class KitCirurgicoListCreateView(generics.ListCreateAPIView):
    queryset = KitCirurgico.objects.filter(is_active=True)
    serializer_class = KitCirurgicoSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["codigo", "nome"]


class KitCirurgicoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KitCirurgico.objects.all()
    serializer_class = KitCirurgicoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class KitItemListCreateView(generics.ListCreateAPIView):
    queryset = KitItem.objects.filter(is_active=True)
    serializer_class = KitItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["kit"]


class KitItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KitItem.objects.all()
    serializer_class = KitItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
