# Generated by Django 3.0.3 on 2020-03-18 03:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200318_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]