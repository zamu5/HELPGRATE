# Generated by Django 3.0.4 on 2020-03-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20200311_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.SlugField(primary_key=True, serialize=False, unique=True),
        ),
    ]
