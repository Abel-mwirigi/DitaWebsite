from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm

def hardware(request):
    template = loader.get_template('hardware.html')
    return HttpResponse(template.render())

def login(request):
   if request.method == 'POST':
       form = UserForm(request.POST)
       if form.is_valid():
           form.save()
   else:
       form = UserForm()
   return render(request, 'login.html', {'form': form})
