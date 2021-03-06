# Generated by Django 3.2.9 on 2021-12-16 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0051_auto_20211216_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='commerce.service'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_image',
            field=models.ImageField(default=1, upload_to='service/', verbose_name='image'),
            preserve_default=False,
        ),
    ]
