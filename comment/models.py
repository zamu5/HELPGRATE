from django.contrib.auth.models import User
from task.models import Task
from django.db import models


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return f'{self.owner} - {self.task}'
