# Generated by Django 5.1.1 on 2024-09-24 20:54

import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_date_of_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='mediafiles', validators=[petstagram.photos.validators.FileSizeValidator(5)]),
        ),
    ]