from comment.views import CommentCreateView, CommentListView
from django.urls import path

app_name = 'comment'

urlpatterns = [
    path('comments/create/<slug:pk_task>', CommentCreateView.as_view(), name='create_comment'),
    path('comments/<slug:pk_task>', CommentListView.as_view(), name='list_comment'),
]
