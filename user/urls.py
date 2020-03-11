from user.views import CurrentUser
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('', CurrentUser.as_view(), name='current'),
]
