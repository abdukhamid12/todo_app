# Generated by Django 5.0.6 on 2024-07-09 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_is_delete_task_is_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_deleted',
            new_name='is_delete',
        ),
    ]
