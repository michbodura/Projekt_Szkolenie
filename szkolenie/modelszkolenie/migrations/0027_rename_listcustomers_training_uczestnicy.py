# Generated by Django 3.2.6 on 2021-08-05 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0026_alter_training_listcustomers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='listCustomers',
            new_name='uczestnicy',
        ),
    ]
