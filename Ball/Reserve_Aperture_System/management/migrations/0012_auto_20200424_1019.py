# Generated by Django 3.0.4 on 2020-04-24 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20200424_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='expires_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 10, 19, 58, 622696)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='leave_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
