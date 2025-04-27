from django.urls import path
from . import views

# Padroes de URL para o app 'eventos'
urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('participacoes/', views.lista_participacoes, name='lista_participacoes'),
]