# Generated by Django 4.0.7 on 2023-03-13 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtc_bus_ticketing_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRoutes',
            fields=[
                ('BusRoute_No', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Source_location', models.CharField(max_length=50)),
                ('Destination_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='busroutedetails',
            name='BusRoute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtc_bus_ticketing_app.busroutes'),
        ),
    ]
