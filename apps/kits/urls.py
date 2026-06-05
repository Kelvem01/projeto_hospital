from django.urls import path
from . import views

urlpatterns = [
    path("", views.KitCirurgicoListCreateView.as_view(), name="kit-list"),
    path("<int:pk>/", views.KitCirurgicoDetailView.as_view(), name="kit-detail"),
    path("itens/", views.KitItemListCreateView.as_view(), name="kititem-list"),
    path("itens/<int:pk>/", views.KitItemDetailView.as_view(), name="kititem-detail"),
]
