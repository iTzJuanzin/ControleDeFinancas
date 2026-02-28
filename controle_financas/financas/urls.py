from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('adicionar/', views.adicionar, name='adicionar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('exportar/', views.exportar_excel, name='exportar_excel'),
]