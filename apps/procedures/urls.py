from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProcedimentoListCreateView.as_view(), name="procedimento-list"),
    path("<int:pk>/", views.ProcedimentoDetailView.as_view(), name="procedimento-detail"),
]
