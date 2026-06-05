from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/centro-cirurgico/", views.DashboardCentroCirurgicoView.as_view(), name="dashboard-cc"),
    path("dashboard/financeiro/", views.DashboardFinanceiroView.as_view(), name="dashboard-fin"),
    path("dashboard/estoque/", views.DashboardEstoqueView.as_view(), name="dashboard-est"),
    path("ia/analise-ocupacao/", views.AIAnaliseOcupacaoView.as_view(), name="ia-ocupacao"),
    path("ia/analise-financeira/", views.AIAnaliseFinanceiraView.as_view(), name="ia-financeiro"),
    path("ia/relatorio-gerencial/", views.AIRelatorioGerencialView.as_view(), name="ia-relatorio"),
    path("insights/", views.InsightIACreateListView.as_view(), name="insight-list"),
    path("dashboards/", views.DashboardListCreateView.as_view(), name="dashboard-list"),
    path("indicadores/", views.IndicadorListCreateView.as_view(), name="indicador-list"),
]
