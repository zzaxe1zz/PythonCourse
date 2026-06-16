from django.http import HttpResponse
from django.shortcuts import render

# def Saludo(request):
#     return HttpResponse('Hola mundo desde Django')


# def Saludo(request):
#     return render(request, 'index.html', {
#         'mensaje': 'Este es un mensaje',
#         'titulo': 'Axel Gomez'
#     })

def Saludo(request):
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
