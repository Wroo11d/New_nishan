# Generated by Django 3.2.9 on 2021-12-15 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0028_auto_20211215_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='close_days',
        ),
        migrations.RemoveField(
            model_name='center',
            name='close_time',
        ),
        migrations.RemoveField(
            model_name='center',
            name='open_time',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='time',
        ),
        migrations.RemoveField(
            model_name='service',
            name='time',
        ),
    ]
