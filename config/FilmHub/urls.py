from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404,handler403
from django.contrib.auth import views as auth_views
handler403 = views.response_error_handler
handler404 = views.page_not_found


urlpatterns = [
    path('', views.HomeView, name="homeView"),
    
    path('about/', views.ContactView.as_view(), name="aboutView"),
    path('register/', views.RegisterView, name="registerView"),
    path('funciones/<str:pelicula>', views.FuncionesView, name="funciones"),
    path('logout/', views.LogoutUser, name="logoutView"),
    path('login/', views.LoginView, name="loginView"),
    path('403/', views.permission_denied_view,name="permisionDenied"),
    path('404/', views.page_not_found_view,name="pagenotfound"),

    path('client/profile/', views.ProfileView, name="profileView"),
    path('client/mytickets/', views.MyTicketsView, name="my_tickets"),
    path('client/buyticket/<int:funcion>', views.BuyTicketView, name="buy_ticket"),
    path('client/buyfood/<int:boleto>', views.BuyFoodView, name="buy_food"),
    path('client/ticketinfo/<int:factura>', views.TicketInfoView, name="ticket_info"),
    


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="FilmHub/password_reset.html"),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="FilmHub/password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="FilmHub/password_reset_form.html"),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="FilmHub/password_reset_complete.html"),name='password_reset_complete'),

]
