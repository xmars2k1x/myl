from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.menu_principal),
    url(r'^crear-cuenta/', views.crear_cuenta),
    url(r'^iniciar-sesion/', views.iniciar_sesion),
    url(r'^cerrar-sesion/', views.cerrar_sesion),
    url(r'^test/', views.test),
]
