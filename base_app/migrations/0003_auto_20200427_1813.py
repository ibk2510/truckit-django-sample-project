# Generated by Django 3.0.5 on 2020-04-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20200427_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckrent',
            name='drop_time',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
