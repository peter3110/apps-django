from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from encuestas.models import *

def data(request):
    data_usuarios = datosUsuarioAnonimo.objects.all()
    data_inflacion = inflacionThomsonReuters.objects.all()
    inflaciones = '[' + ', '.join('(' + str(i.porcentaje) + ', ' + str(i.fecha) + ')' for i in data_inflacion) + ']'
    ciudades = ', '.join([u.ciudad for u in data_usuarios])
    context = {
        'ciudades': ciudades,
        'inflaciones': inflaciones
    }
    return render(request, 'visualizaciones/data.html', context)

def index(request): 
    context = {
        'info': "Hello, world. Esta es la pagina principal de la app 'Visualizaciones' "
    }
    return render(request, 'visualizaciones/index.html', context)


def charts(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response



