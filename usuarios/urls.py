from django.urls import path
from .views import UsuarioLoginView, UsuarioLogoutView, UsuarioSignupView

urlpatterns = [
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('logout/', UsuarioLogoutView.as_view(), name='logout'),
    path('signup/', UsuarioSignupView.as_view(), name='signup'),
]
