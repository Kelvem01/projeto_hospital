from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib.auth import views as auth_views    
from apps.accounts.views import ProfileView

api_patterns = [
    path("accounts/", include("apps.accounts.urls")),
    path("patients/", include("apps.patients.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_patterns)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    
    path("", include("config.frontend_urls")),
    
    # ==================== ACCOUNTS ====================
    path("accounts/login/", auth_views.LoginView.as_view(
        template_name="registration/login.html",
        redirect_authenticated_user=True,
    ), name="login"),
    
    path("accounts/logout/", 
         auth_views.LogoutView.as_view(
             next_page="/",           # ou "login"
             template_name="registration/logged_out.html"  # opcional
         ), 
         name="logout"),
    
    path("accounts/", ProfileView.as_view(), name="accounts"),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)