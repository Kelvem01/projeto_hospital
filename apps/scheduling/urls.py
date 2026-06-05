from django.urls import path
from . import views

urlpatterns = [
    path("", views.CirurgiaListCreateView.as_view(), name="cirurgia-list"),
    path("<int:pk>/", views.CirurgiaDetailView.as_view(), name="cirurgia-detail"),
    path("consumos/", views.ConsumoMaterialListCreateView.as_view(), name="consumo-list"),
]
