# Generated by Django 3.2.8 on 2021-10-18 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransportApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='delivery_time',
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_day',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_hour',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='orders',
            name='lat',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='lon',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
