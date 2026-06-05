from django.urls import path
from . import views

urlpatterns = [
    path("cirurgioes/", views.CirurgiaoListCreateView.as_view(), name="cirurgiao-list"),
    path("cirurgioes/<int:pk>/", views.CirurgiaoDetailView.as_view(), name="cirurgiao-detail"),
    path("anestesistas/", views.AnestesistaListCreateView.as_view(), name="anestesista-list"),
    path("anestesistas/<int:pk>/", views.AnestesistaDetailView.as_view(), name="anestesista-detail"),
    path("especialidades/", views.EspecialidadeListCreateView.as_view(), name="especialidade-list"),
    path("especialidades/<int:pk>/", views.EspecialidadeDetailView.as_view(), name="especialidade-detail"),
]
