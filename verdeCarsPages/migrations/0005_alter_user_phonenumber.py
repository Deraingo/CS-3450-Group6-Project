# Generated by Django 4.1.1 on 2023-03-21 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verdeCarsPages', '0004_alter_user_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='000-000-0000', max_length=10),
        ),
    ]
