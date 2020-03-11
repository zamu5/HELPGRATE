from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView
from user.serializers import UserSerializer
from django.contrib.auth.models import User


class CurrentUser(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer



