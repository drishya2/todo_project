# Generated by Django 4.2.5 on 2024-05-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_delete_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]