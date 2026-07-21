from django.urls import path

from . import views

urlpatterns = [
    path('', views.orden, name='orden'),
    path('direccion', views.direccion, name='direccion')
]
