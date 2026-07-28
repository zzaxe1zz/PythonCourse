from django.urls import path

from . import views

urlpatterns = [
    path('', views.orden, name='orden'),
    path('direccion', views.direccion, name='direccion'),
    path('seleccionar/direccion', views.select_direccion, name='select_direccion'),
    path('establecer/direccion/<int:pk>',
         views.check_direccion, name='check_direccion'),
    path('confirmacion/direccion', views.confimacion, name='confirmacion'),
    path('cancelar/direccion', views.cancelar_orden, name='cancelar'),
    path('completado/direccion', views.completado, name='completado'),
    path('completados/direccion', views.OrdenViews.as_view(), name='completados'),
]
