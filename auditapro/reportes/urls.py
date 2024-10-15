from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('camMenu/', views.CamMenu, name='CamMenu'),
    path('mainMenu/', views.mainMenu, name='MainMenu'),
    path('logIn/', views.logIn, name='LogIn'),
    path('lightsMenu/', views.lightsMenu, name='LightsMenu'),
    path('toggle-boolean/', views.toggle_boolean, name='toggle_boolean'),
]
