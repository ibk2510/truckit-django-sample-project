# Generated by Django 3.0.5 on 2020-05-01 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0008_truckrent_is_rejected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='is_requested',
        ),
    ]
