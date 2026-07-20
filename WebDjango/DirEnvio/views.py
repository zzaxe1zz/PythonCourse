from django.shortcuts import render
from .models import DireccionEnvio
from django.views.generic import ListView
from .forms import DireccionesEnviosForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse


class EnvioDirecciones(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = DireccionEnvio
    template_name = 'direccion_envios/direccion_envio.html'

    def get_queryset(self):
        return DireccionEnvio.objects.filter(user=self.request.user).order_by('-default')


@login_required(login_url='login')
def formularioDir(request):
    form = DireccionesEnviosForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        direccion_envio = form.save(commit=False)
        direccion_envio.user = request.user
        direccion_envio.default = not DireccionEnvio.objects.filter(
            user=request.user).exists()
        direccion_envio.save()

        messages.success(request, 'Direccion agregada con exito')
        return redirect('direccion_envio')

    return render(request, 'direccion_envios/formulario.html', {
        'form': form
    })


class UpdateDireccion(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = DireccionEnvio
    form_class = DireccionesEnviosForm
    template_name = 'direccion_envios/actualizar.html'
    success_message = 'Direccion actualizada con exito'

    def get_success_url(self):
        return reverse('direccion_envio')
