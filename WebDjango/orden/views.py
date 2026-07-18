from django.shortcuts import render
from carts.funciones import funcionCarrito
from .models import Orden
from .utils import funcionOrden
from django.contrib.auth.decorators import login_required
from .utils import breadcrumb


@login_required(login_url='login')
def orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)


def orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)
    return render(request, 'orden/orden.html', {
        'cart': cart,
        'orden': orden,
        'breadcrumb': breadcrumb(),
    })
