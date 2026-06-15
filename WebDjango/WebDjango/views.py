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
        'mensaje': 'Ingreso',
        'titulo': 'Personas',
        'personas': [
            {'titulo': 'Axel', 'edad': 21, 'adulto': True},
            {'titulo': 'Diana', 'edad': 21, 'adulto': True},
            {'titulo': 'Esmeralda', 'edad': 17, 'adulto': False}
        ]
    })
