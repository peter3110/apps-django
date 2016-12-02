from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Esta es la pagina principal de la app 'Encuestas' ")

def preguntas(request):
	return HttpResponse("Hello, world. Esta es la pagina de preguntas de la app 'Encuestas' ")