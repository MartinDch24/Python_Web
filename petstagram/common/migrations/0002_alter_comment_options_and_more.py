# Generated by Django 5.1.1 on 2024-10-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_of_publication']},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['date_of_publication'], name='common_comm_date_of_f6820b_idx'),
        ),
    ]
