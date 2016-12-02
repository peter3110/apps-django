from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# ListView / DetailView: 'display a list of objects' and 'display a detail 
# page for a particular type of object.'

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
	# question = get_object_or_404(Question, pk=question_id) # otra opcion
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
    	# CUIDADO!!! ACA FALTA EVITAR RACE CONDITIONS
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button. reverse redirije a '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

###########################################
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button

def sliders(request):
	button = Button(label="Foo", button_type="success")

	template = loader.get_template('polls/sliders.html')
	script, div = components(widgetbox(button))
	context = {
		'var': 1,
		'the_script': script,
		'the_div': div
	}
	return HttpResponse('hola') #HttpResponse(template.render(context,request))
	#return render(request, 'polls/sliders.html', context) #HttpResponse('HOLA')

###########################################
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, components

def bokeh_plot(request):
	# Armo el grafico
    plot = figure()
    plot.circle([1,2], [3,4])

    # Armo la HttpResponse
    template = loader.get_template('polls/bokeh_plot.html')
    script, div = components(plot)
    context = {
    	'the_script': script,
    	'the_div': div
    }

    return HttpResponse(template.render(context,request))