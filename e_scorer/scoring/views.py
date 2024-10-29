from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import AdminLoginForm, EventForm, PerfomerForm,JudgeForm,JudgeLoginForm
from .models import Event,Performer,Judge
from django.shortcuts import get_object_or_404



# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            username  = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('manage_event')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form':form})


def judge_login(request):
    if request.method == 'POST':
        form = JudgeLoginForm(request, data=request.POST)
        if form.is_valid():
            username  = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print("given user: {}".format(user))
            # judges = Judge.objects.all()
            # print(judges)
            if user is not None and Judge.objects.filter(user=user).exists():
                login(request, user)
                return redirect('performer_list')
    else:
        form = JudgeLoginForm()
    return render(request, 'judge_login.html', {'form':form})

#EVENT CRUD OPS

def create_event(request):
    if request.method =='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_event')
    else:
        form = EventForm()
    return render(request,'create_event.html',{'form':form})

def manage_event(request):
    events = Event.objects.all()
    return render(request,'manage_event.html',{'events':events})

def update_event(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method =='POST':
        form  = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('manage_event')
        
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html',{'form':form})

def delete_event(request, event_id):
    event = get_object_or_404(Event,id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('manage_event')
    return render(request,'manage_event.html',{'event':Event.objects.all()})


#performer cruds
def performer_list(request):
    performers = Performer.objects.all()
    return render(request,'performer_list.html',{'performers':performers})

def performer_create(request):
    if request.method == 'POST':
        form = PerfomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performer_list')
    else:
        form = PerfomerForm()
    return  render(request,'performer_create.html',{'form':form})

def performer_update(request,id):
    performer = get_object_or_404(Performer, id=id)
    if request.method == 'POST':
        form = PerfomerForm(request.POST, instance=performer)
        if form.is_valid():
            form.save()
            return redirect('performer_list')
    else:
        form = PerfomerForm(instance=performer)
    return render(request,'performer_create.html',{'form':form})

def performer_delete(request, id):
    performer = get_object_or_404(Performer, id=id)
    if request.method == 'POST':
        performer.delete()
        return redirect('performer_list')
    return render(request,'performer_list.html',{'performer':Performer.objects.all()})

#Judges CRUD

def  judge_list(request):
    judges = Judge.objects.all()
    return render(request,'judge_list.html',{'judges':judges})

def judge_create(request):
    if request.method == 'POST':
        form = JudgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judge_list')
    else:
        form = JudgeForm()
    return render(request,'judge_create.html',{'form':form})

def  judge_update(request,id):
    judge = get_object_or_404(Judge, id=id)
    if request.method == 'POST':
        form = JudgeForm(request.POST, instance=judge)
        if form.is_valid():
            form.save()
            return redirect('judge_list')
    else:
        form = JudgeForm(instance=judge)
    return render(request,'judge_create.html',{'form':form})

def judge_delete(request,id):
    judge = get_object_or_404(Judge, id=id)
    if request.method == 'POST':
        judge.delete()
        return redirect('judge_list')
    return render(request,'judge_confirm_delete.html',{'judge':Judge.objects.all()})




