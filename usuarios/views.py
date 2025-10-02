from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

class UsuarioLoginView(LoginView):
    template_name = 'usuarios/login.html'
    

class UsuarioLogoutView(LogoutView):
    template_name = 'usuarios/logout2.html'


class UsuarioSignupView(CreateView):
    form_class = RegistroForm
    template_name = 'usuarios/signup.html'
    success_url = reverse_lazy('login')

# Create your views here.
