# Generated by Django 3.2 on 2021-04-29 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 16, 3, 15, 904373)),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 16, 3, 15, 904373)),
        ),
    ]