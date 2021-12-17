# Generated by Django 3.2.9 on 2021-12-16 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commerce', '0054_auto_20211216_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copinion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Copinions', to='commerce.center')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Copinions', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sopinion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sopinions', to='commerce.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sopinions', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='opinion',
        ),
    ]
