# Generated by Django 3.2.6 on 2021-08-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0003_remove_szkolenie_gosc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gosc',
            options={'verbose_name_plural': 'Gość'},
        ),
        migrations.AlterModelOptions(
            name='odpowiedz',
            options={'verbose_name_plural': 'Odpowiedź'},
        ),
        migrations.AlterField(
            model_name='szkolenie',
            name='obraz',
            field=models.ImageField(upload_to='images/szkolenie'),
        ),
    ]
