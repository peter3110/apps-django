from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory

from .models import inflacionThomsonReuters, datosUsuarioAnonimo
from .forms import datosUsuarioAnonimoForm

def index(request):
    return HttpResponse("Hello, world. Esta es la pagina principal de la app 'Encuestas' ")

def graficos(request, context):
    #return HttpResponse("Aca van los graficos obtenidos a partir de los datos de la form")
    return render(request, 'graficos/grafico1.html', context)

def preguntas(request):
    welcome_str = "Hello, world. Esta es la pagina de preguntas de la app 'Encuestas' "

    # A HTTP POST?
    if request.method == 'POST':
        form = datosUsuarioAnonimoForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return graficos(request, {'form': form})
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = datosUsuarioAnonimoForm()

    context = {
        'form': form, 
        'welcome_str': welcome_str
    }
    return render(request, 'encuestas/preguntas.html', context)


