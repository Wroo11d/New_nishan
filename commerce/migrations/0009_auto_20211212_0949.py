# Generated by Django 3.2.9 on 2021-12-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_auto_20211212_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='image',
            field=models.ImageField(default=0, upload_to='advertisings/', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='center',
            name='image',
            field=models.ImageField(default=0, upload_to='centers/', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='sercive_image',
            field=models.ImageField(default=0, upload_to='service/', verbose_name='service_image'),
            preserve_default=False,
        ),
    ]
