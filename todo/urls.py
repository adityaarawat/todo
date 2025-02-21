from django.urls import path
from .import views

urlpatterns=[
    path('addTask/', views.addTask, name='addTask'),
    #mark comppleted
    path('markAsCompelted/<int:pk>/',views.markAsCompelted,name='markComplete'),
    # mark undone
    path('markAsUndone/<int:pk>/',views.markAsUndone,name='markAsUndone'),
    # update
    path('updateTask/<int:pk>/',views.updateTask,name='updateTask'),
    #Delete
    path('deletedTask/<int:pk>/',views.deletedTask,name='deletedTask'),
]