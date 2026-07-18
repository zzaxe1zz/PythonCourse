from django.shortcuts import render
from .models import DireccionEnvio
from django.views.generic import ListView
from .forms import DireccionesEnviosForm


class EnvioDirecciones(ListView):
    model = DireccionEnvio
    template_name = 'direccion_envios/direccion_envio.html'

    def get_queryset(self):
        return DireccionEnvio.objects.filter(user=self.request.user).order_by('-default')


def formularioDir(request):
    form = DireccionesEnviosForm()
    return render(request, 'direccion_envios/formulario.html', {
        'form': form
    })
