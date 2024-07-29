
from django.urls import path
from AppHernan import views 

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('socios/', views.socios, name="Socios"),
    path('acreditaciones/', views.acreditaciones, name="Acreditaciones"),
    path('deportes/', views.deportes, name="Deportes"),
    path('entregables/', views.entregables, name="Entregables"),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),
    path('mostrar-deportes/', views.mostrar_deportes, name="Mostrar_Deportes"),
]
