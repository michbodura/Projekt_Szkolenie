# Generated by Django 3.2.6 on 2021-08-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0039_alter_galeryimage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='obowiazkowe',
            field=models.BooleanField(default=False),
        ),
    ]