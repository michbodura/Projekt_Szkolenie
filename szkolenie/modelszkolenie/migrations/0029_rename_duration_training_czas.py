# Generated by Django 3.2.6 on 2021-08-05 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0028_alter_training_uczestnicy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='duration',
            new_name='czas',
        ),
    ]