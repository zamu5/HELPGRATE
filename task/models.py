from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from uuid import uuid4


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    helper = models.ManyToManyField(User, related_name='helper', blank=True)
    id = models.SlugField(primary_key=True, unique=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    owner = models.ManyToManyField(User)
    description = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Task)
def my_handler(sender, **kwargs):
    slug_id = uuid4()

    if not kwargs['instance'].id:
        for _ in range(8):
            if not Task.objects.filter(id=slug_id).exists():
                kwargs['instance'].id = slug_id
                break
