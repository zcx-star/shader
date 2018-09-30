from django.http import HttpResponse,HttpResponseRedirect  
from django.shortcuts import render,render_to_response,get_object_or_404
from django import forms
from django.utils import timezone
from .models import Shader

def index(request): 
    shader_list = Shader.objects.order_by('shader_name')

    '''
    v=0
    sql = "SELECT * FROM shader_shader WHERE shader_vertexColor=%s" %(v)
    b=Shader.objects.raw(sql)
    '''



    if request.method=="POST":
        selected_vertexColor = request.POST['selectVertexColor'] 
        selected_uvSet = request.POST['selectUVSet']
        selected_surfaceType = request.POST['selectSurfaceType']

        sql="SELECT * FROM shader_shader WHERE shader_surfaceType=%s" %(selected_surfaceType)
        selected_shader=Shader.objects.raw(sql)

        return render(request, 'shader/index.html', 
        {'shader_list':shader_list,'selected_shader':selected_shader,
        'selected_vertexColor':selected_vertexColor,'selected_uvSet':selected_uvSet,
        'selected_surfaceType':selected_surfaceType
        })

    return render(request, 'shader/index.html', {'shader_list':shader_list,'selected_shader':shader_list})

def detail(request,shader_name):
    shader_list = Shader.objects.order_by('shader_name')
    shader = get_object_or_404(Shader, pk = shader_name)
    t = 'shader/detail/' + shader_name + '.html'
    return render(request, t, {'shader':shader, 'shader_list':shader_list})