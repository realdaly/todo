from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("", views.apiOverview, name="apiOverview"),
    path("taskList/", views.taskList, name="taskList"),
    path("taskDetail/<int:pk>/", views.taskDetail, name="taskDetail"),
    path("taskCreate/", views.taskCreate, name="taskCreate"),
    path("taskUpdate/<int:pk>", views.taskUpdate, name="taskUpdate"),
    path("taskDelete/<int:pk>", views.taskDelete, name="taskDelete"),
]