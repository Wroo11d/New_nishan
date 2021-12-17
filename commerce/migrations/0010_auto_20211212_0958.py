# Generated by Django 3.2.9 on 2021-12-12 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0009_auto_20211212_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=0, upload_to='service/', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='center',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='commerce.center'),
            preserve_default=False,
        ),
    ]
