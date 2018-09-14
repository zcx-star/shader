from django.http import HttpResponse,HttpResponseRedirect  
from django.shortcuts import render,render_to_response,get_object_or_404
from django import forms
from django.utils import timezone
from .models import Shader

def index(request):		
    shader_list = Shader.objects.order_by('shader_name')
    if request.method == "POST":   
    	try:
        	selected_shader = shader_list.filter(shader_opaque = request.POST['selectOpaque'])
    	except (KeyError, Shader.DoesNotExist):  
            selected_shader = shader_list    
        
        try:
            selected_shader_1 = shader_list.filter(shader_uv = request.POST['selectUV'])
        except (KeyError, Shader.DoesNotExist):  
            selected_shader_1 = shader_list
     
    	return render(request, 'shader/index.html', {'shader_list':shader_list,'selected_shader':selected_shader})

    else:
    	return render(request, 'shader/index.html', {'shader_list':shader_list,'selected_shader':shader_list})

def detail(request,shader_name):
    shader = get_object_or_404(Shader, pk = shader_name)
    return render(request, 'shader/detail.html', {'shader':shader})