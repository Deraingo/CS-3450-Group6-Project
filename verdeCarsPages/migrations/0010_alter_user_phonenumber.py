# Generated by Django 4.1.2 on 2023-04-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0009_alter_car_checkoutcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='000-000-0000', max_length=12),
        ),
    ]