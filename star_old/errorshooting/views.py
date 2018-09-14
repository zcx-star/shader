from django.http import HttpResponse,HttpResponseRedirect  
from django.shortcuts import render,render_to_response
from django import forms
from django.utils import timezone
from errorshooting.models import *

from .models import BugPic

class SubmitPic(forms.Form):
    user = forms.CharField()
    img = forms.ImageField()

class VoteProblem(forms.Form):
    id = forms.IntegerField()

def index(request):
    pic_list = BugPic.objects.order_by('id')
    if request.method == "POST":   
        #submit error pic                     
        if "submit_bugpic" in request.POST:
            submitted = SubmitPic(request.POST,request.FILES)
            if submitted.is_valid():
                bug_pic = BugPic()
                bug_pic.user = submitted.cleaned_data['user']
                bug_pic.img = submitted.cleaned_data['img']
                bug_pic.time = timezone.now()
                bug_pic.save()
                return HttpResponseRedirect('/errorshooting')
        #vote for problem
        elif "submit_problem" in request.POST:            
            submitted = VoteProblem(request.POST)
            if submitted.is_valid():
                vote_id= submitted.cleaned_data['id']
                vote = BugPic.objects.filter(pk= vote_id)
                vote = vote[0]
                vote.vote_problem += 1
                vote.save()
                return HttpResponseRedirect('/errorshooting')
        else:
            return HttpResponseRedirect('/errorshooting')
    else: 
        submitted = SubmitPic()

    #input in panel_submit binds with 'submitted':submitted here
    return render(request,'errorshooting/index.html',{'submitted':submitted,'pic_list':pic_list})
