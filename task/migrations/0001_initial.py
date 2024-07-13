# Generated by Django 5.0.6 on 2024-07-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha...')),
                ('description', models.TextField(verbose_name='Tavsif:')),
                ('is_done', models.BooleanField(default=False, verbose_name='Bajarildi')),
                ('is_delete', models.BooleanField(default=False, verbose_name='O`chirildi')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Topshiriq',
                'verbose_name_plural': 'Topshiriqlar',
                'ordering': ['-updated_at'],
            },
        ),
    ]
