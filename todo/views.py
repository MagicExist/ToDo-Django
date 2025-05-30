from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import task

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task.objects.create(title=title,description=description)
            return redirect('index')
    else:
        form = TaskForm()

    ctx = {'title':'index','name':'MagicExist','form':form}
    return render(request,'todo/index.html',ctx)