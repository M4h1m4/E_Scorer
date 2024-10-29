from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import AdminLoginForm, EventForm
from .models import Event
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

