from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
)


app_name = 'marketplace'

urlpatterns = [
    path('', ProductoListView.as_view(), name='lista_productos'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('producto/nuevo/', ProductoCreateView.as_view(), name='nuevo_producto'),
    
]
