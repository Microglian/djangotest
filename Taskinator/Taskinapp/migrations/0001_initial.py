# Generated by Django 5.0.6 on 2024-06-01 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('is_scheduled', models.BooleanField(default=False)),
                ('schedule_datetime', models.DateTimeField()),
                ('schedule_duration', models.DurationField(default=3600)),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed'), ('A', 'Archived')], default='O', max_length=1)),
                ('assignees', models.ManyToManyField(to='Taskinapp.user')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='Taskinapp.user')),
            ],
        ),
    ]
