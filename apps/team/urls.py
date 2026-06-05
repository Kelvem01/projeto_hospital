from django.urls import path
from . import views

urlpatterns = [
    path("profissionais/", views.ProfissionalEnfermagemListCreateView.as_view(), name="profissional-list"),
    path("profissionais/<int:pk>/", views.ProfissionalEnfermagemDetailView.as_view(), name="profissional-detail"),
    path("equipes/", views.EquipeCirurgiaListCreateView.as_view(), name="equipe-list"),
    path("equipes/<int:pk>/", views.EquipeCirurgiaDetailView.as_view(), name="equipe-detail"),
    path("presencas/", views.RegistroPresencaListCreateView.as_view(), name="presenca-list"),
    path("trocas/", views.TrocaPlantaoListCreateView.as_view(), name="troca-list"),
]
