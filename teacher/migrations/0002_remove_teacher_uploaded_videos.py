# Generated by Django 2.0.7 on 2021-02-18 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='uploaded_videos',
        ),
    ]