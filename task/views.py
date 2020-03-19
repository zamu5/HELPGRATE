from django.db.models import Q
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from task.serializers import TaskSerializer, TaskSerializerDetail, TaskHelperSerializer, TaskUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from task.permissions import Isowner
from task.models import Task


class TaskDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs.get('pk'))


class TaskUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, Isowner]
    serializer_class = TaskUpdateSerializer

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs.get('pk'))


class TaskUpdateHelperView(UpdateAPIView):
    serializer_class = TaskHelperSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs.get('pk'))

    def get_object(self):
        obj = super(TaskUpdateHelperView, self).get_object()
        obj.helper.add(self.request.user)
        return obj


class TaskDetailView(RetrieveAPIView):
    serializer_class = TaskSerializerDetail
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs.get('pk'))


class TaskCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        request.data['owner'] = (request.user.pk,)

        return super(TaskCreateView, self).create(request, *args, **kwargs)


class TasksListCommunityView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TasksListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        filters = ~Q(helper=self.request.user)
        return Task.objects.filter(filters)


class TasksListHelperView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(helper=self.request.user)
