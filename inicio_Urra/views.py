from django.shortcuts import render

# Mock data for topics
TEMAS = [
    {
        'id': 1,
        'nombre': 'Tema 1',
        'descripcion': 'Descubre los artistas más influyentes y escucha sobre sus grandes éxitos en la industria musical.',
        'portada_emoji': '🎤',
        'imagenes': ['images/cantante1.png', 'images/cantante2.png']
    },
    {
        'id': 2,
        'nombre': 'Tema 2',
        'descripcion': 'Explora la velocidad y el diseño de los automóviles más asombrosos del mundo.',
        'portada_emoji': '🚘',
        'imagenes': ['images/auto1.png', 'images/auto2.png']
    }
]

def inicio(request):
    return render(request, 'inicio_Urra/inicio.html', {'temas': TEMAS})

def tema_detalle(request, tema_id):
    tema = next((t for t in TEMAS if t['id'] == tema_id), None)
    if not tema:
        from django.http import Http404
        raise Http404("Tema no encontrado")

    return render(request, 'inicio_Urra/tema_detalle.html', {'tema': tema})
