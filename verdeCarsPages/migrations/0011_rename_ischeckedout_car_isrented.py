# Generated by Django 4.0.2 on 2023-04-12 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0010_car_ischeckedout_alter_user_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='isCheckedOut',
            new_name='isRented',
        ),
    ]