from django.urls import path
from . import frontend_views

urlpatterns = [
    # Dashboard e outras páginas
    path("", frontend_views.dashboard, name="dashboard"),
    path("dashboard/", frontend_views.dashboard, name="dashboard"),

    path("patients/", frontend_views.patient_list, name="patient-list"),
    path("patients/create/", frontend_views.patient_create, name="patient-create"),

    path("surgeries/", frontend_views.surgery_list, name="surgery-list"),
    path("surgeries/create/", frontend_views.surgery_create, name="surgery-create"),

    path("operating-rooms/", frontend_views.room_list, name="room-list"),
    path("procedures/", frontend_views.procedure_list, name="procedure-list"),
    path("kits/", frontend_views.kit_list, name="kit-list"),
    path("inventory/", frontend_views.material_list, name="material-list"),
    path("consumo/", frontend_views.consumo_list, name="consumo-list"),
    path("admissions/", frontend_views.admission_list, name="admission-list"),

    path("doctors/", frontend_views.doctor_list, name="doctor-list"),
    path("nursing/", frontend_views.nursing_list, name="nursing-list"),
    path("circulantes/", frontend_views.circulante_list, name="circulante-list"),

    path("billing/", frontend_views.billing_list, name="billing-list"),
    path("reports/", frontend_views.report_list, name="report-list"),
    path("ai-insights/", frontend_views.ai_insights, name="ai-insights"),
]