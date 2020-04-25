# Generated by Django 3.0.5 on 2020-04-25 05:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20200425_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='manager_manag_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Manager'),
        ),
        migrations.AlterField(
            model_name='company',
            name='expires_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 25, 12, 40, 43, 352896)),
        ),
    ]
