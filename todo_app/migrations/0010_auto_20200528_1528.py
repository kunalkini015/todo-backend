# Generated by Django 2.2.6 on 2020-05-28 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0009_auto_20200528_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
