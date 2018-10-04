from django.http import HttpResponse,HttpResponseRedirect  
from django.shortcuts import render,render_to_response,get_object_or_404
from django import forms
from django.utils import timezone
from .models import Shader

def switchBooleam(selected):
    temp = 'all'
    if selected == 'True':
        temp = '1'
    elif selected == 'False':
        temp = '0'
    return temp

def switchType(selected):
    temp = 'all'
    if selected =='Opqaue':
        temp = '0'
    elif selected =='Transparent':
        temp = '1'
    elif selected =='Translucent':
        temp = '2'
    return temp

def index(request): 
    shader_list = Shader.objects.order_by('shader_name')

    if request.method=="POST":
        selected_vertexColor  = request.POST['selectVertexColor']   
        s_0 = switchBooleam(selected_vertexColor) 

        selected_uvSet        = request.POST['selectUVSet']

        selected_surfaceType  = request.POST['selectSurfaceType']
        s_2 = switchType(selected_surfaceType)

        selected_complexity   = request.POST['selectComplexity']
        selected_textures     = request.POST['selectTextures']
        selected_diffuseTex   = request.POST['selectDiffuseTex']
        selected_normalTex    = request.POST['selectNormalTex']
        selected_SMDTex       = request.POST['selectSMDTex']
        selected_uvTint       = request.POST['selectUvTint']
        s_8 = switchBooleam(selected_uvTint)
        selected_maskTint     = request.POST['selectMaskTint']
        s_9 = switchBooleam(selected_maskTint)
        selected_globalDirt   = request.POST['selectGlobalDirt']
        s_10 = switchBooleam(selected_globalDirt)
        selected_emissive     = request.POST['selectEmissive']
        s_11 = switchBooleam(selected_emissive)
        selected_wetness      = request.POST['selectWetness']
        s_12 = switchBooleam(selected_wetness)
        selected_parallax     = request.POST['selectParallax']
        s_13 = switchBooleam(selected_parallax)
        selected_retroReflect = request.POST['selectRetroReflect']
        s_14 = switchBooleam(selected_retroReflect)

        selected = [s_0,selected_uvSet,s_2,selected_complexity,selected_textures,selected_diffuseTex,selected_normalTex,selected_SMDTex,s_8,s_9,s_10,s_11,s_12,s_13,s_14]
        allNum = selected.count('all')

        sql = "SELECT * FROM shader_shader"
        attach = ""
        judgeNum = 15
        judgements = [
        'shader_vertexColor',
        'shader_uvSet',
        'shader_surfaceType',
        'shader_complexity',
        'shader_textures',
        'shader_diffuseTex',
        'shader_normalTex',
        'shader_SMDTex',
        'shader_uvTint',
        'shader_maskTint',
        'shader_globalDirt',
        'shader_emissive',
        'shader_wetness',
        'shader_parallax',
        'shader_retroReflect']

        if allNum == (judgeNum-1):
            for i in range(judgeNum):
                if selected[i] != 'all':
                    attach += " WHERE "+judgements[i]+" = "+selected[i]
        elif allNum != judgeNum:
            attach += " WHERE "
            for i in range(judgeNum):
                if selected[i] != 'all':
                    attach += judgements[i]+" = "+selected[i]+" AND "
            attach = attach[:-5]

        sql = sql + attach

        selected_shader=Shader.objects.raw(sql)

        return render(request, 'shader/index.html',{
            "shader_list":shader_list,
            "selected_shader":selected_shader,
            "selected_vertexColor":selected_vertexColor,
            "selected_uvSet":selected_uvSet,
            "selected_surfaceType":selected_surfaceType,
            "selected_complexity":selected_complexity,
            "selected_textures":selected_textures,
            "selected_diffuseTex":selected_diffuseTex,
            "selected_normalTex":selected_normalTex,
            "selected_SMDTex":selected_SMDTex,
            "selected_uvTint":selected_uvTint,
            "selected_maskTint":selected_maskTint,
            "selected_globalDirt":selected_globalDirt,
            "selected_emissive":selected_emissive,
            "selected_wetness":selected_wetness,
            "selected_parallax":selected_parallax,
            "selected_retroReflect":selected_retroReflect,
            'sql':sql,
            'allNum':allNum,
            's_2':s_2
            })

    return render(request, 'shader/index.html', {'shader_list':shader_list,'selected_shader':shader_list})

def detail(request,shader_name):
    shader_list = Shader.objects.order_by('shader_name')
    shader = get_object_or_404(Shader, pk = shader_name)
    temp = 'shader/detail/' + shader_name + '.html'
    return render(request, temp, {'shader':shader, 'shader_list':shader_list})