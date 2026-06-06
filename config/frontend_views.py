from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages


@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, "Você saiu da conta com sucesso.")
    return redirect("/")          # ou redirect("dashboard")

def logout_view(request):
    auth_logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    from apps.rooms.models import SalaCirurgica
    from apps.scheduling.models import Cirurgia
    from apps.billing.models import Faturamento
    from datetime import date

    salas = SalaCirurgica.objects.filter(is_active=True)
    stats = {
        "total_salas": salas.count(),
        "salas_disponiveis": salas.filter(status="disponivel").count(),
        "salas_ocupadas": salas.filter(status="ocupada").count(),
        "salas_manutencao": salas.filter(status="manutencao").count(),
        "taxa_ocupacao": round(salas.filter(status="ocupada").count() / max(salas.count(), 1) * 100, 1),
        "cirurgias_hoje": Cirurgia.objects.filter(data=date.today(), is_active=True).count(),
    }

    receita_mensal = 0
    from django.db.models import Sum, F
    from datetime import date
    mes_atual = date.today().replace(day=1)
    fat = Faturamento.objects.filter(
        data_emissao__gte=mes_atual, status__in=["pago", "parcial"], is_active=True
    )
    for f in fat:
        receita_mensal += f.calcular_valor_total()

    context = {
        "stats": stats,
        "receita_mensal": f"{receita_mensal:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        "breadcrumbs": [{"label": "Dashboard", "url": None}],
    }
    return render(request, "dashboard/index.html", context)


@login_required
def patient_list(request):
    from apps.patients.models import Paciente
    pacientes = Paciente.objects.filter(is_active=True).select_related("convenio")
    return render(request, "patients/list.html", {
        "pacientes": pacientes,
        "breadcrumbs": [{"label": "Pacientes", "url": None}],
    })


@login_required
def patient_create(request):
    from apps.patients.models import Convenio, Paciente
    if request.method == "POST":
        from django.utils import timezone
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        rg = request.POST.get("rg", "")
        email = request.POST.get("email", "")
        telefone = request.POST.get("telefone", "")
        profissao = request.POST.get("profissao", "")
        data_nascimento = request.POST.get("data_nascimento") or None
        convenio_id = request.POST.get("convenio") or None
        numero_carteirinha = request.POST.get("numero_carteirinha", "")

        if nome and cpf:
            Paciente.objects.create(
                nome=nome, cpf=cpf, rg=rg, email=email, telefone=telefone,
                profissao=profissao,
                data_nascimento=data_nascimento if data_nascimento else None,
                convenio_id=convenio_id, numero_carteirinha=numero_carteirinha,
            )
            messages.success(request, "Paciente cadastrado com sucesso!")
            return redirect("patient-list")
        messages.error(request, "Nome e CPF são obrigatórios.")

    return render(request, "patients/create.html", {
        "convenios": Convenio.objects.filter(is_active=True),
        "breadcrumbs": [
            {"label": "Pacientes", "url": "/patients/"},
            {"label": "Cadastro", "url": None},
        ],
    })


@login_required
def surgery_list(request):
    from apps.scheduling.models import Cirurgia
    cirurgias = Cirurgia.objects.filter(is_active=True).select_related(
        "paciente", "procedimento", "sala", "cirurgiao"
    )
    return render(request, "surgeries/list.html", {
        "cirurgias": cirurgias,
        "breadcrumbs": [{"label": "Cirurgias", "url": None}],
    })


@login_required
def surgery_create(request):
    from apps.patients.models import Paciente, Convenio
    from apps.procedures.models import Procedimento
    from apps.rooms.models import SalaCirurgica
    from apps.doctors.models import Cirurgiao
    from apps.scheduling.models import Cirurgia

    if request.method == "POST":
        try:
            Cirurgia.objects.create(
                paciente_id=request.POST.get("paciente"),
                procedimento_id=request.POST.get("procedimento"),
                sala_id=request.POST.get("sala"),
                cirurgiao_id=request.POST.get("cirurgiao"),
                data=request.POST.get("data"),
                hora_inicio=request.POST.get("hora_inicio"),
                hora_prevista_termino=request.POST.get("hora_prevista_termino"),
                convenio_id=request.POST.get("convenio") or None,
                observacoes=request.POST.get("observacoes", ""),
            )
            messages.success(request, "Cirurgia agendada com sucesso!")
            return redirect("surgery-list")
        except Exception as e:
            messages.error(request, f"Erro ao agendar: {e}")

    return render(request, "surgeries/create.html", {
        "pacientes": Paciente.objects.filter(is_active=True),
        "procedimentos": Procedimento.objects.filter(is_active=True),
        "salas": SalaCirurgica.objects.filter(is_active=True),
        "cirurgioes": Cirurgiao.objects.filter(is_active=True),
        "convenios": Convenio.objects.filter(is_active=True),
        "breadcrumbs": [
            {"label": "Cirurgias", "url": "/surgeries/"},
            {"label": "Agendamento", "url": None},
        ],
    })


@login_required
def room_list(request):
    from apps.rooms.models import SalaCirurgica
    salas = SalaCirurgica.objects.filter(is_active=True)
    context = {
        "salas": salas,
        "salas_disponiveis": salas.filter(status="disponivel").count(),
        "salas_ocupadas": salas.filter(status="ocupada").count(),
        "salas_manutencao": salas.filter(status="manutencao").count(),
        "taxa_ocupacao": round(salas.filter(status="ocupada").count() / max(salas.count(), 1) * 100, 1),
        "breadcrumbs": [{"label": "Salas Cirúrgicas", "url": None}],
    }
    return render(request, "operating_rooms/list.html", context)


@login_required
def procedure_list(request):
    from apps.procedures.models import Procedimento
    procedimentos = Procedimento.objects.filter(is_active=True).select_related("especialidade")
    return render(request, "procedures/list.html", {
        "procedimentos": procedimentos,
        "breadcrumbs": [{"label": "Procedimentos", "url": None}],
    })


@login_required
def kit_list(request):
    from apps.kits.models import KitCirurgico
    kits = KitCirurgico.objects.filter(is_active=True).prefetch_related("itens__material")
    return render(request, "procedures/kit_list.html", {
        "kits": kits,
        "breadcrumbs": [
            {"label": "Procedimentos", "url": "/procedures/"},
            {"label": "Kits Cirúrgicos", "url": None},
        ],
    })


@login_required
def material_list(request):
    from apps.materials.models import Material
    materiais = Material.objects.filter(is_active=True).select_related("categoria")
    criticos = sum(1 for m in materiais if m.is_estoque_critico())
    return render(request, "inventory/list.html", {
        "materiais": materiais,
        "criticos": criticos,
        "total_materiais": materiais.count(),
        "breadcrumbs": [{"label": "Materiais", "url": None}],
    })


@login_required
def consumo_list(request):
    from apps.scheduling.models import ConsumoMaterialCirurgia
    consumos = ConsumoMaterialCirurgia.objects.select_related(
        "cirurgia__paciente", "material"
    ).order_by("-created_at")[:100]
    return render(request, "inventory/consumo.html", {
        "consumos": consumos,
        "breadcrumbs": [
            {"label": "Estoque", "url": "/inventory/"},
            {"label": "Consumo", "url": None},
        ],
    })


@login_required
def doctor_list(request):
    from apps.doctors.models import Cirurgiao, Anestesista
    cirurgioes = Cirurgiao.objects.filter(is_active=True).prefetch_related("especialidades")
    anestesistas = Anestesista.objects.filter(is_active=True)
    return render(request, "equipes/doctors.html", {
        "cirurgioes": cirurgioes,
        "anestesistas": anestesistas,
        "breadcrumbs": [{"label": "Médicos", "url": None}],
    })


@login_required
def nursing_list(request):
    from apps.team.models import ProfissionalEnfermagem
    profissionais = ProfissionalEnfermagem.objects.filter(is_active=True)
    return render(request, "equipes/nursing.html", {
        "profissionais": profissionais,
        "breadcrumbs": [{"label": "Enfermagem", "url": None}],
    })


@login_required
def circulante_list(request):
    from apps.team.models import TrocaPlantao
    trocas = TrocaPlantao.objects.select_related(
        "equipe__cirurgia", "circulante_saida", "circulante_entrada"
    ).order_by("-data_hora_troca")[:100]
    return render(request, "equipes/circulantes.html", {
        "trocas": trocas,
        "breadcrumbs": [{"label": "Circulantes", "url": None}],
    })


@login_required
def billing_list(request):
    from apps.billing.models import Faturamento
    from datetime import date
    faturas = Faturamento.objects.filter(is_active=True).select_related("paciente", "convenio")
    receita_mensal = 0
    mes_atual = date.today().replace(day=1)
    for f in faturas.filter(data_emissao__gte=mes_atual, status__in=["pago", "parcial"]):
        receita_mensal += f.calcular_valor_total()
    pendentes = faturas.filter(status="pendente").count()
    return render(request, "billing/list.html", {
        "faturas": faturas,
        "receita_mensal": f"{receita_mensal:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        "pendentes": pendentes,
        "breadcrumbs": [{"label": "Faturamento", "url": None}],
    })


@login_required
def report_list(request):
    return render(request, "reports/list.html", {
        "breadcrumbs": [{"label": "Relatórios", "url": None}],
    })


@login_required
def ai_insights(request):
    return render(request, "ai_insights/index.html", {
        "breadcrumbs": [{"label": "IA Insights", "url": None}],
    })


@login_required
def admission_list(request):
    from apps.admissions.models import Internacao
    internacoes = Internacao.objects.filter(is_active=True).select_related("paciente", "leito").order_by("-data_entrada")
    return render(request, "surgeries/admissions.html", {
        "internacoes": internacoes,
        "breadcrumbs": [{"label": "Internações", "url": None}],
    })
