from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto
from .forms import ProductoForm


class ProductoListView(ListView):
    model = Producto
    template_name = 'marketplace/lista.html'
    context_object_name = 'productos'
    ordering = ['-fecha_publicacion']
    paginate_by = 12

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'marketplace/detalle.html'
    context_object_name = 'producto'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'marketplace/form.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('marketplace:detalle_producto', kwargs={'pk': self.object.pk})
