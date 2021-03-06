# Generated by Django 3.2 on 2021-05-04 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 5, 4, 14, 59, 29, 421141))),
                ('modified_at', models.DateTimeField(default=datetime.datetime(2021, 5, 4, 14, 59, 29, 422139))),
                ('username', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 5, 4, 14, 59, 29, 421141))),
                ('modified_at', models.DateTimeField(default=datetime.datetime(2021, 5, 4, 14, 59, 29, 421141))),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(choices=[('SA', 'Saudi Arabia'), ('FR', 'Out of Saudi Arabia'), ('NA', 'Prefer not to say')], default='Prefer not to say', max_length=250)),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
