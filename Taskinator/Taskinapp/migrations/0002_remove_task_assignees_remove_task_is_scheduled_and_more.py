# Generated by Django 5.0.6 on 2024-06-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Taskinapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assignees',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_scheduled',
        ),
        migrations.RemoveField(
            model_name='task',
            name='schedule_datetime',
        ),
        migrations.RemoveField(
            model_name='task',
            name='schedule_duration',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
