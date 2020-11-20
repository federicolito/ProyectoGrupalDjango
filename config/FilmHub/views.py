from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator

from .decorators import unauthenticated_user
from .forms import CreateUserForm, UserForm
from .models import *
from django.views.generic import TemplateView






# Create your views here.
@unauthenticated_user
def LoginView(request):
    context= {}
    
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request , username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homeView')
        else :
            messages.error(request, "Username OR password is incorrect " )
            return render(request, 'FilmHub/login.html' , context)
    
    return render(request, 'FilmHub/login.html' , context)

@unauthenticated_user
def RegisterView(request):
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, "Account was created for " + username)
            return redirect('loginView')
    context= {
        'form':form
    }
    return render(request, 'FilmHub/register.html' , context)


def LogoutUser(request):
    logout(request)
    return redirect('loginView')


@login_required(login_url='login')
def FuncionesView(request,pelicula):
    pelicula = Pelicula.objects.get(pk=pelicula)
    now = datetime.datetime.now()
    funciones = Funcion.objects.filter(pelicula=pelicula,horario__gte=now)
    

    
    context= {
    'pelicula':pelicula,
    'funciones':funciones}
    return render(request, 'FilmHub/funciones.html', context)
def HomeView(request):
    peliculas = Pelicula.objects.all()


    paginator = Paginator(peliculas,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'peliculas':page_obj}
    return render(request, 'FilmHub/home.html',context)


    

@login_required(login_url='login')
def ProfileView(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    context= {'form':form}
    return render(request, 'FilmHub/profile.html', context)



class ContactView(TemplateView):
    template_name = "FilmHub/about.html"
  

def response_error_handler(request, exception=None):
    return HttpResponse('Error handler content', status=403)

def permission_denied_view(request):
    return HttpResponse('you dont have acces here')

def page_not_found(request, exception=None,template_name='FilmHub/404.html'):
    return render('Error handler content', status=404)

def page_not_found_view(request):
    return render(request, 'FilmHub/404.html')

