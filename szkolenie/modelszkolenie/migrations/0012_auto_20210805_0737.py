# Generated by Django 3.2.6 on 2021-08-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0011_alter_firma_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='obrazdogalerii',
            options={'ordering': ['-data'], 'verbose_name_plural': 'Galeria'},
        ),
        migrations.AlterField(
            model_name='obrazdogalerii',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
