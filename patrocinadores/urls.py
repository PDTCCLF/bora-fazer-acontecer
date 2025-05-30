from django.urls import path
from . import views

# Padroes de URL para o app 'patrocinadores'
urlpatterns = [
    path('', views.lista_patrocinadores, name='lista_patrocinadores'),
    path('financiamentos/', views.lista_financiamentos, name='lista_financiamentos'),
    path('criar/', views.criar_patrocinador, name='criar_patrocinador'),
    path('financiamentos/criar/', views.criar_financiamento, name='criar_financiamento'),
    path('<int:pk>/editar/', views.editar_patrocinador, name='editar_patrocinador'),
    path('financiamentos/<int:pk>/editar/', views.editar_financiamento, name='editar_financiamento'),
    path('<int:pk>/deletar/', views.deletar_patrocinador, name='deletar_patrocinador'),
    path('financiamentos/<int:pk>/deletar/', views.deletar_financiamento, name='deletar_financiamento'),
]