from django.urls import path, include
from .views import (TaskListApiView, TaskDetail)



urlpatterns = [
    path('api/', TaskListApiView.as_view()),
    path('api/<int:pk>/', TaskDetail.as_view())
]