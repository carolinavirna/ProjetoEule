from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home',),
    path('inserir/', views.inserir, name='inserir'),
    path('banco_de_questoes/<str:cat>/', views.banco_de_questoes, name='responder'),
    path('disciplinas/', views.disciplinas, name='disciplinas'),
    path('perfil/', views.perfil, name='perfil'),
]