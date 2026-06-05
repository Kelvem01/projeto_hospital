from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InsightIA, Dashboard, Indicador
from .serializers import InsightIASerializer, DashboardSerializer, IndicadorSerializer
from .services import DashboardService, AIService


class DashboardCentroCirurgicoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        service = DashboardService()
        data = service.get_centro_cirurgico_stats()
        return Response(data)


class DashboardFinanceiroView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        service = DashboardService()
        data = service.get_financeiro_stats()
        return Response(data)


class DashboardEstoqueView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        service = DashboardService()
        data = service.get_estoque_stats()
        return Response(data)


class AIAnaliseOcupacaoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        ai = AIService()
        if not ai.is_available():
            return Response(
                {"detail": "IA não disponível. Configure OPENAI_API_KEY."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        analise = ai.gerar_analise_ocupacao()
        return Response({"analise": analise})


class AIAnaliseFinanceiraView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        ai = AIService()
        if not ai.is_available():
            return Response(
                {"detail": "IA não disponível. Configure OPENAI_API_KEY."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        analise = ai.gerar_analise_financeira()
        return Response({"analise": analise})


class AIRelatorioGerencialView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        ai = AIService()
        relatorio = ai.gerar_relatorio_gerencial()
        return Response({"relatorio": relatorio})


class InsightIACreateListView(generics.ListCreateAPIView):
    queryset = InsightIA.objects.all()
    serializer_class = InsightIASerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["tipo", "data_referencia"]
    ordering_fields = ["-created_at"]


class DashboardListCreateView(generics.ListCreateAPIView):
    queryset = Dashboard.objects.filter(is_active=True)
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndicadorListCreateView(generics.ListCreateAPIView):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = [permissions.IsAuthenticated]
