# Generated by Django 4.1.1 on 2023-03-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0002_alter_car_cost_alter_user_money_alter_user_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='000-000-0000', max_length=10),
        ),
    ]