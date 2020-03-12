from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from task.serializers import TaskSerializer
from task.permissions import Isowner
from task.models import Task


class TaskDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs.get('pk'))


class TaskUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, Isowner]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs.get('pk'))


class TaskDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs.get('pk'))


class TaskCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        request.data['owner'] = (request.user.pk,)

        return super(TaskCreateView, self).create(request, *args, **kwargs)


class TasksListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TasksListHelperView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(helper=self.request.user)
