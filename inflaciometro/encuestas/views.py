from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory

from .models import inflacionThomsonReuters, datosUsuarioAnonimo
from .forms import datosUsuarioAnonimoForm

def index(request):
    return HttpResponse("Hello, world. Esta es la pagina principal de la app 'Encuestas' ")

def make_plot():
    from bokeh.plotting import figure, output_file, show 
    from bokeh.embed import components

    x= [1,3,5,7,9,11,13]
    y= [1,2,3,4,5,6,7]
    title = 'y = f(x)'

    plot = figure(title= title , 
        x_axis_label= 'X-Axis', 
        y_axis_label= 'Y-Axis', 
        plot_width =400,
        plot_height =400)

    plot.line(x, y, legend= 'f(x)', line_width = 2)
    return components(plot)

def graficos(request, context):
    from django.shortcuts import render, render_to_response
    
    script, div = make_plot()
    context['title'] = "Aca van los graficos a partir de los datos: "
    context['script'] = script
    context['div'] = div
    return render_to_response('graficos/grafico1.html', context)

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
            return graficos(request, {'data': form.cleaned_data})
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


