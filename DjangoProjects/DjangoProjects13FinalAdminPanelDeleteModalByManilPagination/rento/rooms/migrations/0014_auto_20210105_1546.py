# Generated by Django 3.1.4 on 2021-01-05 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0013_auto_20210105_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rooms.city'),
        ),
    ]