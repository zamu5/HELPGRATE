# Generated by Django 3.0.4 on 2020-03-11 17:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0004_task_helper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='helper',
            field=models.ManyToManyField(blank=True, null=True, related_name='helper', to=settings.AUTH_USER_MODEL),
        ),
    ]
