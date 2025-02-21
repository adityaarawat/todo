from django.urls import path
from .import views

urlpatterns=[
    path('addTask/', views.addTask, name='addTask'),
    path('markAsCompelted/<int:pk>/',views.markAsCompelted,name='markComplete'),
    path('markAsUndone/<int:pk>/',views.markAsUndone,name='markAsUndone')
]