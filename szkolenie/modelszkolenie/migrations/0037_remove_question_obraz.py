# Generated by Django 3.2.6 on 2021-08-06 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0036_auto_20210805_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='obraz',
        ),
    ]