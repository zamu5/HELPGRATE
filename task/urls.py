from task.views import TasksListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.urls import path

app_name = 'task'

urlpatterns = [
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='update_task'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/create', TaskCreateView.as_view(), name='create_task'),
    path('tasks/', TasksListView.as_view(), name='list_tasks'),
]
