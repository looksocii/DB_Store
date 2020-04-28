# Generated by Django 3.0.5 on 2020-04-23 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20200420_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperture',
            name='aper_pic',
            field=models.ImageField(default=None, upload_to='C:/Users/LilAop/Desktop/django_projects/Reserve_Aperture_System/media'),
        ),
        migrations.AlterField(
            model_name='aperture',
            name='store_store_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='management.Store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_pic',
            field=models.ImageField(default=None, upload_to='C:/Users/LilAop/Desktop/django_projects/Reserve_Aperture_System/media'),
        ),
    ]