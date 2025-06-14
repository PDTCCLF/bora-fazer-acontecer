from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Padroes de URL para o app 'core'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
]