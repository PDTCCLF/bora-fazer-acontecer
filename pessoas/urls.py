from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),
]
