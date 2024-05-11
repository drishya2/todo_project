from django.shortcuts import render, redirect
from . models import Task

# Create your views here.
def add(request):

    if request.method=='POST':
        task=request.POST['task']
        tasks=Task.objects.create(task=task)
        tasks.save()
        return redirect('/')
    else:
        tasks=Task.objects.all()
        return render(request,'home.html',{'tasks':tasks})

def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('/')

def update(request,id):
    task=Task.objects.get(id=id)
    task.status=True
    task.save()
    return redirect('/')