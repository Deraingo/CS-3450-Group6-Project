# Generated by Django 4.1.1 on 2023-03-04 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0007_alter_car_year_alter_user_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='availability',
            new_name='available',
        ),
    ]
