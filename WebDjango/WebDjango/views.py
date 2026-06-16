from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages

# def Saludo(request):
#     return HttpResponse('Hola mundo desde Django')


# def Saludo(request):
#     return render(request, 'index.html', {
#         'mensaje': 'Este es un mensaje',
#         'titulo': 'Axel Gomez'
#     })

def Index(request):
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Tienda',
        'articulos': [
            {'titulo': 'Sudadera', 'precio': 15, 'stock': False},
            {'titulo': 'Pantalon', 'precio': 11, 'stock': True},
            {'titulo': 'Playera', 'precio': 18, 'stock': False},
            {'titulo': 'Gorra', 'precio': 10, 'stock': True}
        ]
    })


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        usuarios = authenticate(username=username, password=password)
        if usuarios:
            lg(request, usuarios)
            messages.success(request, f'Bienvenido {usuarios.username}')
            return redirect('Index')
        else:
            messages.error(request, 'Usuario  contraseña incorrectas')
            print()

    return render(request, 'user/login.html', {})
