from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib import messages
from login.forms import loginForm
from django.core.urlresolvers import reverse

@sensitive_post_parameters()
@csrf_protect
@never_cache
def auth_login(request):
    """ Verificar si el usuario esta autenticado, si lo esta redireccionar a la vista """
    if request.user.is_authenticated():
        redirect(reverse('colegios.index'))

    if request.method == "POST":
    	form = loginForm(request.POST)

    	if form.is_valid():
    		form = loginForm(request.POST)
    		username = request.POST['username']
        	password = request.POST['password']
        	user = authenticate(username=username, password=password)
   			
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('colegios.index'))
            else:
                messages.add_message(request, messages.ERROR, "Cuenta Inactiva.")
        else:
             messages.add_message(request, messages.ERROR, "Usuario o Password Invalidos")
    		
        return render(request, 'registration/login.html',{'form': form})
    form = loginForm()                 
    return render(request, 'registration/login.html',{'form': form})
  
def logout_view(request):

    if request.user.is_authenticated():
        logout(request)
        messages.add_message(request, messages.SUCCESS, \
            'You have been successfully logged out.')
    else:
        messages.add_message(request, messages.INFO, \
            'Only authenticated users can be logged out.')
    return redirect(reverse('login.login'))