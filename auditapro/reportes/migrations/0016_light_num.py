# Generated by Django 4.2.7 on 2023-11-16 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0015_alter_light_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='light',
            name='num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
