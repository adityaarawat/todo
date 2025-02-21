from django.shortcuts import redirect,get_object_or_404,render

from .models import Tasks
from django.http import HttpResponse
# Create your views here.
def addTask(request):
    task=request.POST['task']
    Tasks.objects.create(task=task)
    return redirect("home")

def markAsCompelted(request,pk):
    task=get_object_or_404(Tasks, pk=pk)
    task.is_completed=True
    task.save()
    return redirect("home")

def markAsUndone(request,pk):
    task=get_object_or_404(Tasks, pk=pk)
    task.is_completed=False
    task.save()
    return redirect("home")

def deletedTask(request,pk):
    deleteTask=get_object_or_404(Tasks,pk=pk)
    deleteTask.delete()
    return redirect('home')

def updateTask(request,pk):
    getTask=get_object_or_404(Tasks, pk=pk)
    if request.method=='POST':
        newTask=request.POST['task']
        getTask.task=newTask
        getTask.save()
        print(newTask)
        return redirect('home')
    else :
        context={
        'getTask':getTask
        }
        return render(request,'update.html',context)
    

