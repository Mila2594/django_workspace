from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, Mundo! Esta es la vista de inicio.")