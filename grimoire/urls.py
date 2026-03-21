from django.urls import path
from .import views

urlpatterns = [
    path('wizards/', views.wizards, name='wizards'),
    path('cadastro/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('editar/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('deletar/<int:id>/', views.deletar_pessoa, name='deletar_pessoa'),
    path('personagens-hp', views.lista_hp, name="lista_hp"),
]