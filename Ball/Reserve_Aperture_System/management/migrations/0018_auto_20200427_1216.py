# Generated by Django 3.0.5 on 2020-04-27 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_auto_20200425_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='expires_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 12, 16, 15, 84704)),
        ),
    ]
