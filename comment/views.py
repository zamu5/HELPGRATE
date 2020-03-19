from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from comment.serializers import CommentSerializer
from comment.models import Comment


class CommentCreateView(CreateAPIView):
    permission_classes = []
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        request.data['task'] = kwargs.get('pk_task')
        request.data['owner'] = request.user.pk

        return super(CommentCreateView, self).create(request, *args, **kwargs)


class CommentListView(ListAPIView):
    permission_classes = []
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(task=self.kwargs.get('pk_task'))[:16]
