# Generated by Django 4.1.2 on 2023-01-24 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
