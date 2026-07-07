from django.shortcuts import render
from .models import Cart
from products.models import Product
from .funciones import funcionCarrito
# Create your views here.


def cart(request):
    cart = funcionCarrito(request)

    return render(request, 'cart/cart.html', {'cart': cart})


def add(request):
    cart = funcionCarrito(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.producs.add(product)

    return render(request, 'cart/add.html', {
        'product': product
    })
