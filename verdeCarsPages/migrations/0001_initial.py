# Generated by Django 4.1.1 on 2023-03-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='', max_length=50)),
                ('model', models.CharField(default='', max_length=50)),
                ('year', models.CharField(default='0000', max_length=4)),
                ('cost', models.FloatField()),
                ('rentalStart', models.DateField()),
                ('rentalEnd', models.DateField()),
                ('checkoutCode', models.IntegerField()),
                ('stranded', models.BooleanField(default=False)),
                ('imageURL', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('usernm', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('userType', models.CharField(default='Customer', max_length=50)),
                ('money', models.FloatField(default=0.0)),
                ('phoneNumber', models.CharField(default='000-000-0000', max_length=10)),
            ],
        ),
    ]
