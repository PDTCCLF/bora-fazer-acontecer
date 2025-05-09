from django.urls import path
from . import views

# Padroes de URL para o app 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
]