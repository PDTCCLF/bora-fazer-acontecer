from django.urls import path
from . import views

# Padroes de URL para o app 'eventos'
urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('participacoes/', views.lista_participacoes, name='lista_participacoes'),
    path('criar/', views.criar_evento, name='criar_evento'),
    path('criar_participacao/', views.criar_participacao, name='criar_participacao'),
    path('editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('editar_participacao/<int:pk>/', views.editar_participacao, name='editar_participacao'),
    path('deletar/<int:pk>/', views.deletar_evento, name='deletar_evento'),
    path('deletar_participacao/<int:pk>/', views.deletar_participacao, name='deletar_participacao'),
]