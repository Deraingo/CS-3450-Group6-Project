# Generated by Django 4.0.2 on 2023-04-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0012_alter_car_strandedaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='strandedAddress',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
