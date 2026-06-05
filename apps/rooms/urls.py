from django.urls import path
from . import views

urlpatterns = [
    path("", views.SalaCirurgicaListCreateView.as_view(), name="sala-list"),
    path("<int:pk>/", views.SalaCirurgicaDetailView.as_view(), name="sala-detail"),
]
