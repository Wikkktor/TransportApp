# Generated by Django 3.2.8 on 2021-10-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransportApp', '0004_alter_orders_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery_hour',
            field=models.TimeField(),
        ),
    ]
