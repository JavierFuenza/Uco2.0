from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'pagina/Index.html', context)
def registrar(request):
    context={}
    return render(request, 'pagina/registro.html', context)
def nosotros(request):
    context={}
    return render(request, 'pagina/Nosotros.html', context)
def pantalones(request):
    context={}
    return render(request, 'pagina/pantalones.html', context)
def poleras(request):
    context={}
    return render(request, 'pagina/poleras.html', context)
def polerones(request):
    context={}
    return render(request, 'pagina/polerones.html', context)