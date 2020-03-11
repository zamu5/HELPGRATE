from user.views import CurrentUser, CreateUser
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('', CurrentUser.as_view(), name='current'),
    path('create', CreateUser.as_view(), name='create_user'),
]
