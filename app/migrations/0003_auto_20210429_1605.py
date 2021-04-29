# Generated by Django 3.2 on 2021-04-29 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210429_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 4, 29, 16, 5, 43, 131333))),
                ('modified_at', models.DateTimeField(default=datetime.datetime(2021, 4, 29, 16, 5, 43, 131333))),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(choices=[('Saudi Arabia', 'SA'), ('Out of Saudi Arabia', 'FR'), ('Prefer not to say', 'NA')], default='Prefer not to say', max_length=250)),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='visitors',
        ),
    ]
