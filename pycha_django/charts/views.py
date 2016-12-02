# Create your views here.

from StringIO import StringIO
from django.http import HttpResponse
from django.shortcuts import render_to_response

import cairo

XML_PREAMBLE = '<?xml version="1.0" encoding="UTF-8"?>'


def colors_chart(inline = False):
    """
    Generate colours chart

    Set inline to True to disable the XML preamble
    """
    in_req = 1
    
    svg_buffer = StringIO()
    
    width, height = (500, 400)
    surface = cairo.SVGSurface(svg_buffer, width, height)
    
    dataSet = (
     ('dataSet 1', ((0, 1), (1, 3), (2, 2.5))),
     ('dataSet 2', ((0, 2), (1, 4), (2, 3))),
     ('dataSet 3', ((0, 5), (1, 1), (2, 0.5))),     
    )
    
    options = {
       'legend': {'hide': True},
       'background': {'color': '#f0f0f0'},
    }
    
    import pycha.bar
    chart = pycha.bar.VerticalBarChart(surface, options)

    #import pycha.line
    #chart = pycha.line.LineChart(surface, options)
    chart.addDataset(dataSet)
    chart.render()
    
    del chart
    del surface
    
    response = ''

    if inline:
        svg_buffer.seek(len(XML_PREAMBLE))
    else:
        svg_buffer.seek(0)
    return svg_buffer.read()


def colors_svg(request):
    """ render a pure SVG chart """
    response = HttpResponse(mimetype='image/svg+xml')
    response.write(colors_chart(inline = False))
    return response
    
def index(request):
    """ render a chart into the template """
    chart_svg = colors_chart(inline = True)

    return render_to_response(
        'shapes_index.html',
        { "chart" : chart_svg },
        mimetype='application/xhtml+xml')



