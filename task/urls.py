from django.urls import path
from .views import TaskList,TaskCreate

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task-create/", TaskCreate.as_view(), name="task_create"),
]