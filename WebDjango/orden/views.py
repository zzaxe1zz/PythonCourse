from django.shortcuts import get_object_or_404, redirect, render
from .models import DireccionEnvio
from carts.funciones import funcionCarrito, deleteCart
from .models import Orden
from .utils import funcionOrden, deleteOrden
from django.contrib.auth.decorators import login_required
from .utils import breadcrumb
from django.contrib import messages
from DirEnvio.models import DireccionEnvio
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import EmptyQuerySet


class OrdenViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'orden/ordenes.html'

    def get_queryset(self):
        return self.request.user.ordenes_completadas()


# def orden(request):
#     cart = funcionCarrito(request)
#     orden = funcionOrden(cart, request)
@login_required(login_url='login')
def orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)
    return render(request, 'orden/orden.html', {
        'cart': cart,
        'orden': orden,
        'breadcrumb': breadcrumb(),
    })


@login_required(login_url='login')
def direccion(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)

    direccion_envio = orden.get_or_set_direccion_envio()
    countDireccion = request.user.direccionenvio_set.count() > 1

    return render(request, 'orden/direccion.html', {
        'cart': cart,
        'orden': orden,
        'direccion_envio': direccion_envio,
        'countDireccion': countDireccion,
        'breadcrumb': breadcrumb(address=True),
    })


@login_required(login_url='login')
def select_direccion(request):
    direccion_envios = request.user.direccionenvio_set.all()
    return render(request, 'orden/select_direccion.html', {
        'breadcrumb': breadcrumb(address=True),
        'direccion_envios': direccion_envios
    })


@login_required(login_url='login')
def check_direccion(request, pk):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)

    direccion_envio = get_object_or_404(DireccionEnvio, pk=pk)
    if request.user.id != direccion_envio.user_id:
        return redirect('Index')

    orden.update_direccion_envio(direccion_envio)

    return redirect('direccion')


@login_required(login_url='login')
def confimacion(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)

    direccion_envio = orden.direccion_envio
    if direccion_envio is None:
        return redirect('direccion')

    return render(request, 'orden/confirmacion.html', {
        'cart': cart,
        'orden': orden,
        'direccion_envio': direccion_envio,
        'breadcrumb': breadcrumb(address=True, confimation=True),

    })


@login_required(login_url='login')
def cancelar_orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)

    if request.user.id != orden.user_id:
        return redirect('Index')

    orden.cancelar()
    deleteCart(request)
    deleteOrden(request)

    messages.error(request, 'Orden eliminada correctamente')
    return redirect('Index')


@login_required(login_url='login')
def completado(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)

    if request.user.id != orden.user_id:
        return redirect('Index')

    orden.completado()
    deleteCart(request)
    deleteOrden(request)

    messages.success(request, 'Compra completada')
    return redirect('Index')
