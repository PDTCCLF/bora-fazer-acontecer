from django.urls import path
from . import views

# Padroes de URL para o app 'pessoas'
urlpatterns = [
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('alunos/criar/', views.criar_aluno, name='criar_aluno'),
    path('alunos/<int:pk>/editar/', views.editar_aluno, name='editar_aluno'),
    path('alunos/<int:pk>/deletar/', views.deletar_aluno, name='deletar_aluno'),
    path('voluntarios/criar/', views.criar_voluntario, name='criar_voluntario'),
    path('voluntarios/<int:pk>/editar/', views.editar_voluntario, name='editar_voluntario'),
    path('voluntarios/<int:pk>/deletar/', views.deletar_voluntario, name='deletar_voluntario'),
]