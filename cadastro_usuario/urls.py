from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.logar, name='login_user'),
    path('registrar/', views.create_usuario, name='create_user'),
    path('update/', views.update_user, name='update_user'),
    path('delete/', views.delete_user, name='delete_user'),
    path('home/', views.home, name='home'),
    path('usuarios/', views.read_usuario, name='listagem_usuarios'),
    path('logout/', views.logout_user, name='logout_user'),
]