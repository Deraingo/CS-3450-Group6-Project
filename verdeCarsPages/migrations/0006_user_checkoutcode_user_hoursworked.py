# Generated by Django 4.1.1 on 2023-03-21 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0005_alter_user_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='checkoutCode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='hoursWorked',
            field=models.IntegerField(default=0),
        ),
    ]