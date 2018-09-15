from django.http import HttpResponse,HttpResponseRedirect  
from django.shortcuts import render,render_to_response,get_object_or_404
from django import forms
from django.utils import timezone
from .models import Shader

def index(request):		
    shader_list = Shader.objects.order_by('shader_name')

    if request.method == "POST":
        selected_opaque = request.POST['selectOpaque'] 
        selected_uv = request.POST['selectUV']

        if selected_opaque  == 'all':
            q1 = Shader.objects.all()
        else:
            q1 = Shader.objects.filter(shader_opaque = selected_opaque)

        if selected_uv == 'all':
            q2 = Shader.objects.all()
        else:
            selected_uv = int(selected_uv)
            q2 = Shader.objects.filter(shader_uv = selected_uv )
        
        selected_shader = q1.intersection(q2)
        return render(request, 'shader/index.html', {'shader_list':shader_list,'selected_shader':selected_shader, 'selected_opaque':selected_opaque, 'selected_uv':selected_uv})

    return render(request, 'shader/index.html', {'shader_list':shader_list,'selected_shader':shader_list})

def detail(request,shader_name):
    shader = get_object_or_404(Shader, pk = shader_name)
    return render(request, 'shader/detail.html', {'shader':shader})