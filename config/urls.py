from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.shortcuts import redirect   # ← Adicione esta linha

api_patterns = [
    path("accounts/", include("apps.accounts.urls")),
    path("patients/", include("apps.patients.urls")),
    path("doctors/", include("apps.doctors.urls")),
    path("rooms/", include("apps.rooms.urls")),
    path("procedures/", include("apps.procedures.urls")),
    path("materials/", include("apps.materials.urls")),
    path("kits/", include("apps.kits.urls")),
    path("scheduling/", include("apps.scheduling.urls")),
    path("team/", include("apps.team.urls")),
    path("admissions/", include("apps.admissions.urls")),
    path("billing/", include("apps.billing.urls")),
    path("analytics/", include("apps.analytics.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_patterns)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    
    # ✅ Adicione esta linha (redireciona a raiz para o Swagger)
    path('', lambda request: redirect('swagger-ui', permanent=False)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)