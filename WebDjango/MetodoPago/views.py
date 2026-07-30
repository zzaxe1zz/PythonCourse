import stripe
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Asignar la API Key leyendo directamente de settings
stripe.api_key = getattr(settings, 'STRIPE_PRIVATE_KEY', None) or getattr(
    settings, 'STRIPE_SECRET_KEY', None)


@login_required(login_url='login')
def crear(request):
    # Crear el SetupIntent
    intent = stripe.SetupIntent.create(
        payment_method_types=['card'],
    )

    context = {
        'client_secret': intent.client_secret,
        'stripe_public_key': getattr(settings, 'STRIPE_PUBLIC_KEY', ''),
    }

    return render(request, 'metodos_pago/profile_pago.html', context)
