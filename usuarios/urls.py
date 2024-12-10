from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
]