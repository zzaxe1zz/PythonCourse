from django.shortcuts import render
from .models import Cart
from products.models import Product
from .funciones import funcionCarrito
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import CartProduct


def cart(request):
    cart = funcionCarrito(request)
    cart_items = CartProduct.objects.filter(
        cart=cart).select_related('product')

    total_items = sum([item.quantity for item in cart_items])

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_items': total_items,
    })


def add(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    quantity = int(request.POST.get('quantity', 1))

    try:
        cart_product = CartProduct.objects.get(cart=cart, product=product)
        cart_product.quantity += quantity
        cart_product.save()
    except CartProduct.DoesNotExist:
        CartProduct.objects.create(
            cart=cart, product=product, quantity=quantity)

    if hasattr(cart, 'update_totals'):
        cart.update_totals()

    return redirect('cart')


def remove(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('cart')
