# Generated by Django 3.1.1 on 2020-10-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0004_auto_20201010_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_field',
            name='music_file',
            field=models.FileField(upload_to='music/'),
        ),
    ]
