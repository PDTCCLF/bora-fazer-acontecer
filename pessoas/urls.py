from django.urls import path
from . import views

# Padroes de URL para o app 'pessoas'
urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
]