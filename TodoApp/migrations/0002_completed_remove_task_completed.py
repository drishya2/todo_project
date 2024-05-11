# Generated by Django 4.2.5 on 2024-05-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]