from django.shortcuts import redirect,get_object_or_404

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