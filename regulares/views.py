from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import contactos

# Create your views here.
def home (request):
    query = request.GET.get('busqueda')
    filter = request.GET.get('filtro')
    coincidencias = None
    if query and filter:
        lookup = f'{filter}__icontains'
        coincidencias = contactos.objects.filter(Q(**{lookup: query}))
    # contacts = list(contactos.objects.all())
    return render(request, 'index.html', {'coincidencias': coincidencias})