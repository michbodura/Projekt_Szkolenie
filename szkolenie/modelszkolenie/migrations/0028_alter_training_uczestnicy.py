# Generated by Django 3.2.6 on 2021-08-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0027_rename_listcustomers_training_uczestnicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='uczestnicy',
            field=models.ManyToManyField(blank=True, null=True, to='modelszkolenie.User'),
        ),
    ]
