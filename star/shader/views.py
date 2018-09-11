from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Shader

def index(request):
    return HttpResponse("Here is Shader")

def Roboto(request):
    shader_list = Shader.objects.order_by('shader_name')
    return render(request, 'shader/index.html', {'shader_list':shader_list})

def detail(request,shader_name):
    shader = get_object_or_404(Shader, pk=shader_name)
    return render(request, 'shader/detail.html', {'shader':shader})

def Test(request):
	return render(request,'shader/test.html',)