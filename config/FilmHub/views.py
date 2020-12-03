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
from .forms import CreateUserForm, UserForm, ComboComidaForm
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


def FuncionesView(request,pelicula):
    pelicula = Pelicula.objects.get(pk=pelicula)

    now = datetime.datetime.now()
    
    funciones = Funcion.objects.filter(pelicula=pelicula,horario__gte=now)
    


    
    context= {
    'pelicula':pelicula,
    'funciones':funciones}
    return render(request, 'FilmHub/funciones.html', context)

@login_required(login_url='loginView')
def BuyTicketView(request,funcion):
    funcion = Funcion.objects.get(pk=funcion)
    asientos = Asiento.objects.filter(sala=funcion.sala)
    filas =['A','B','C','D','E'] 
    asientosElegidos = []
    asiento = None
    guardarForm = False
    for fila in filas:
        
        for butaca in range(20):
            if request.GET.get(fila+str(butaca)):
                asiento = request.GET.get(fila+str(butaca))
                
                asiento = Asiento.objects.get(pk=asiento)
                asiento.reservado= True
                asiento.save()
                asientosElegidos.append(asiento)
                guardarForm = True

    if guardarForm :
        boleto = Boleto(funcion=funcion)
        boleto.save()
        for asiento in asientosElegidos:
            boleto.asientos.add(asiento)
        boleto.save()
        
        return redirect('buy_food',boleto.pk)
    

                



    
    context= {
    'funcion':funcion,
    'asientos':asientos, 
    'filas':filas
    }
    return render(request, 'FilmHub/buy_ticket.html', context)

@login_required(login_url='loginView')
def BuyFoodView(request, boleto):
    boleto = Boleto.objects.get(pk=boleto)

    form=ComboComidaForm()
    if request.method =="POST":
        form = ComboComidaForm(request.POST)
        if form.is_valid():
            combo_comida = form.save()
            
            messages.success(request, "Su compra se realizó con éxito")
            factura = Factura(boleto=boleto, combo_comida=combo_comida, user=request.user)
            factura.save()
            factura.precio_total()
            return redirect('my_tickets')
        else:
            factura = Factura(boleto=boleto, user=request.user)
            factura.save()
            factura.precio_total()
            return redirect('my_tickets')
    context= {
        'form':form
    }
    context= {
    "boleto":boleto,
    "form":form
    }
    return render(request, 'FilmHub/buy_food.html', context)




@login_required(login_url='loginView')
def MyTicketsView(request):
    facturas = Factura.objects.filter(user=request.user)
    
    now = datetime.datetime.now()
    #,horario__gte=now


    
    context= {
        'facturas':facturas
    }
    return render(request, 'FilmHub/my_tickets.html', context)
def HomeView(request):
    peliculas = Pelicula.objects.all()


    paginator = Paginator(peliculas,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'peliculas':page_obj}
    return render(request, 'FilmHub/home.html',context)


    

@login_required(login_url='loginView')
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

