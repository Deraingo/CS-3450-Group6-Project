# Generated by Django 4.1.1 on 2023-03-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0009_remove_car_available_alter_car_rentalstart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='rentalEnd',
            field=models.DateField(),
        ),
    ]
