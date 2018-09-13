from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice, Shader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

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
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def shaderView(request):		
    shader_list = Shader.objects.order_by('shader_name')
    if request.method == "POST":   
    	try:
        	selected_shader = shader_list.filter(shader_uv = request.POST['selectShader'])
    	except (KeyError, Choice.DoesNotExist):        
        	return render(request, 'polls/error.html')
    	else:
    		return render(request, 'polls/shaderIndex.html', {'shader_list':shader_list,'selected_shader':selected_shader})
    else:
    	return render(request, 'polls/shaderIndex.html', {'shader_list':shader_list,'selected_shader':shader_list})