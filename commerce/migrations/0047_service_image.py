# Generated by Django 3.2.9 on 2021-12-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0046_auto_20211216_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=1, upload_to='service/', verbose_name='image'),
            preserve_default=False,
        ),
    ]
