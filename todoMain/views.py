from django.shortcuts import render
from todo.models import Tasks
def home(request):
    task=Tasks.objects.filter(is_completed=False)
    completed_Task=Tasks.objects.filter(is_completed=True)
    context={
        'tasks':task,
        'completeTask':completed_Task
    }
    return render(request,'index.html',context)