from django.urls import path
from .import views

urlpatterns = [
    path('wizards/', views.wizards, name='wizards'),
    path('cadastro/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
]