# Generated by Django 3.2.9 on 2021-12-16 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0041_auto_20211216_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertising',
            name='center',
        ),
    ]
