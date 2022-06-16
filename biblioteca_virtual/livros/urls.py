from . import views
from django.urls import path

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),
    path('alerta/', views.alerta, name='alerta'),
]
