# Generated by Django 3.2.8 on 2021-10-13 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=300)),
                ('delivery_time', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, 'Nowe'), (2, 'W realizacji'), (3, 'Zrealizowane')], default=1)),
                ('opis', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.cars')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.drivers')),
                ('order', models.ManyToManyField(to='TransportApp.Orders')),
            ],
        ),
    ]
