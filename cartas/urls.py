from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.cartas),
	url(r'^(?P<slug>[-\w]+)/', views.carta)
]
