# Generated by Django 4.2.7 on 2023-11-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0011_usuario_identifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=45)),
                ('status', models.BooleanField(verbose_name=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='camera',
            name='lights',
        ),
    ]
