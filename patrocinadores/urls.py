from django.urls import path
from . import views

# Padroes de URL para o app 'patrocinadores'
urlpatterns = [
    path('', views.lista_patrocinadores, name='lista_patrocinadores'),
    path('financiamentos/', views.lista_financiamentos, name='lista_financiamentos'),
]