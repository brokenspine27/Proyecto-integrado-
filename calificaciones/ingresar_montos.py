from django.urls import path
from . import views

urlpatterns = [
    path('', views.mantenedor_calificaciones, name='mantenedor'),
    path('ingresar/', views.ingresar_calificacion, name='ingresar_calificacion'),
    
    #ruta del formulario de montos
    path('ingresar-montos/<int:calificacion_id>/', views.ingresar_montos, name='ingresar_montos'),
    #ruta de carga masiva con factores
    path('upload/factores/', views.carga_masiva_factores, name='carga_masiva_factores'),
    #ruta de carga masiva con montos
    path('upload/montos/', views.carga_masiva_montos, name='carga_masiva_montos'),
]
