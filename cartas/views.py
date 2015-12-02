from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Carta
import json

@login_required(login_url='/iniciar-sesion/')
def cartas(request):
	cartas = Carta.objects.all()
	paginator = Paginator(cartas, 2)
	page = request.GET.get('page')

	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		p = paginator.page(1)
	except EmptyPage:
		p = paginator.page(paginator.num_pages)

	return render(request, 'cartas.html', {'page': p})

@login_required(login_url='/iniciar-sesion/')
def carta(request, slug):
	carta = get_object_or_404(Carta, slug=slug)
	print(request.user.userprofile.mazo_de_cartas)
	return render(request, 'carta.html', {'carta': carta})
