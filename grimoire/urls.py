from django.urls import path
from .import views

urlpatterns = [
    path('wizards/', views.wizards, name='wizards'),
]