from task.views import TasksListCommunityView, TaskCreateView, TaskUpdateView, TaskDeleteView, TasksListHelperView, \
    TaskDetailView, TasksListView, TaskUpdateHelperView
from django.urls import path

app_name = 'task'

urlpatterns = [
    path('tasks/update/helper/<slug:pk>', TaskUpdateHelperView.as_view(), name='update_task_helper'),
    path('tasks/community', TasksListCommunityView.as_view(), name='list_tasks_community'),
    path('tasks/helper', TasksListHelperView.as_view(), name='list_tasks_helper'),
    path('tasks/detail/<slug:pk>', TaskDetailView.as_view(), name='detail_task'),
    path('tasks/update/<slug:pk>', TaskUpdateView.as_view(), name='update_task'),
    path('tasks/delete/<slug:pk>', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/create', TaskCreateView.as_view(), name='create_task'),
    path('tasks/', TasksListView.as_view(), name='list_tasks'),
]
