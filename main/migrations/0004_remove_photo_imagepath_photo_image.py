# Generated by Django 5.0 on 2023-12-21 14:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_photo_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='imagePath',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product_images/'),
        ),
    ]