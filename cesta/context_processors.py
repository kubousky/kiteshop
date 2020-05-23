from .cesta import Cesta

def cesta(request):
    return {'cesta': Cesta(request)}

    