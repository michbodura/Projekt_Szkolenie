# Generated by Django 3.2.6 on 2021-08-05 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0024_auto_20210805_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='duration',
            field=models.DurationField(verbose_name=datetime.timedelta(days=1)),
        ),
    ]
