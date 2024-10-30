from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  login_required
from .models import Judge

def judge_required(function):
    def wrap(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('judge_login')
        try:
            Judge.objects.get(user=request.user)
            print("inside decorator")
            return function(request,*args,**kwargs)
        except:
            print("Exception occurred")
            return redirect('judge_login')
    return wrap
            


