# Generated by Django 5.1.6 on 2025-02-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_tasks_created_at_alter_tasks_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
