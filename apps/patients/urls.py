from django.urls import path
from . import views

urlpatterns = [
    path("", views.PacienteListCreateView.as_view(), name="paciente-list"),
    path("<int:pk>/", views.PacienteDetailView.as_view(), name="paciente-detail"),
    path("convenios/", views.ConvenioListCreateView.as_view(), name="convenio-list"),
    path("convenios/<int:pk>/", views.ConvenioDetailView.as_view(), name="convenio-detail"),
]
