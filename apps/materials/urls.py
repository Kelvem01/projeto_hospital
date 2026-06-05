from django.urls import path
from . import views

urlpatterns = [
    path("", views.MaterialListCreateView.as_view(), name="material-list"),
    path("<int:pk>/", views.MaterialDetailView.as_view(), name="material-detail"),
    path("categorias/", views.CategoriaMaterialListCreateView.as_view(), name="categoria-list"),
    path("categorias/<int:pk>/", views.CategoriaMaterialDetailView.as_view(), name="categoria-detail"),
    path("movimentos/", views.MovimentoEstoqueListCreateView.as_view(), name="movimento-list"),
]
