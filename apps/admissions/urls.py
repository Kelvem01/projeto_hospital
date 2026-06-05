from django.urls import path
from apps.admissions import views

urlpatterns = [
    path("leitos/", views.LeitoListCreateView.as_view(), name="leito-list"),
    path("leitos/<int:pk>/", views.LeitoDetailView.as_view(), name="leito-detail"),
    path("", views.InternacaoListCreateView.as_view(), name="internacao-list"),
    path("<int:pk>/", views.InternacaoDetailView.as_view(), name="internacao-detail"),
    path("registros/", views.RegistroClinicoListCreateView.as_view(), name="registro-list"),
    path("consumos/", views.ConsumoInternacaoListCreateView.as_view(), name="consumo-list"),
]
