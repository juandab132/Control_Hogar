# Generated by Django 4.2.7 on 2023-11-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0008_camera_number_alter_camera_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='number',
            field=models.IntegerField(max_length=4),
        ),
    ]
