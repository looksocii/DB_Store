# Generated by Django 3.0.5 on 2020-04-23 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20200423_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='expires_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 22, 18, 29, 879169)),
        ),
    ]
