from django.urls import path
from . import views

urlpatterns = [
    path("", views.FaturamentoListCreateView.as_view(), name="faturamento-list"),
    path("<int:pk>/", views.FaturamentoDetailView.as_view(), name="faturamento-detail"),
    path("itens/", views.ItemFaturamentoListCreateView.as_view(), name="item-list"),
    path("itens/<int:pk>/", views.ItemFaturamentoDetailView.as_view(), name="item-detail"),
]
