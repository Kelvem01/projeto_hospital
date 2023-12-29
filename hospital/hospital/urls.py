"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from core import views  #Sherlon: Adicionado para importar as views do meu APP Core
from django.views.generic import RedirectView 
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', views.ola_mundo),
    path('', RedirectView.as_view(url="/home/")), #Definindo a página 'home' como Inicial usando RedirectView
    path('home/', views.home),
    path('home/cliente', RedirectView.as_view(url="/cliente/")),
    path('home/listar_clientes', RedirectView.as_view(url="/cliente/listar_clientes")),
    path('home/cirurgiao', RedirectView.as_view(url="/cirurgiao/")),
    path('home/listar_cirurgioes', RedirectView.as_view(url="/cirurgiao/listar_cirurgioes")),
    path('home/anestesista', RedirectView.as_view(url="/anestesista/")),
    path('home/listar_anestesistas', RedirectView.as_view(url="/anestesista/listar_anestesistas")),
    path('cliente/', views.cliente),
    path('cliente/submit', views.cliente_submit),
    path('cliente/listar_clientes', views.listar_clientes),
    path('cirurgiao/', views.cirurgiao),
    path('cirurgiao/submit', views.cirurgiao_submit),
    path('cirurgiao/listar_cirurgioes', views.listar_cirurgioes),
    path('anestesista/', views.anestesista),
    path('anestesista/submit', views.anestesista_submit),
    path('anestesista/listar_anestesistas', views.listar_anestesistas),
]
