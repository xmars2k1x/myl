from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

def crear_cuenta(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()

	return render(request, 'crear_cuenta.html', {'formulario': formulario})

def iniciar_sesion(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = authenticate(username=request.POST['username'], password=request.POST['password'])
			if usuario is not None:
				login(request, usuario)
				return HttpResponseRedirect('/')
			else:
				error = 'Modificar este texto de error al iniciar sesión'
				return render(request, 'iniciar_sesion.html', {'formulario': formulario, 'error': error})
	else:
		formulario = AuthenticationForm()

	return render(request, 'iniciar_sesion.html', {'formulario': formulario})

@login_required(login_url='/iniciar-sesion/')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/iniciar-sesion/')
def menu_principal(request):
	return render(request, 'menu_principal.html')
