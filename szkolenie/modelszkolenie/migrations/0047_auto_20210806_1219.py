# Generated by Django 3.2.6 on 2021-08-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0046_alter_user_jezyk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='odp',
            field=models.TextField(verbose_name='Odpowiedź'),
        ),
        migrations.AlterField(
            model_name='completedtraining',
            name='data_ukonczenia',
            field=models.DateField(blank=True, null=True, verbose_name='Data ukończenia'),
        ),
        migrations.AlterField(
            model_name='galeryimage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data wstawienia'),
        ),
        migrations.AlterField(
            model_name='question',
            name='jezyk',
            field=models.CharField(blank=True, choices=[('EN', 'Angielski'), ('PL', 'Polski')], max_length=2, null=True, verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tresc',
            field=models.TextField(verbose_name='treść'),
        ),
        migrations.AlterField(
            model_name='questionimage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='questionimage',
            name='tytul',
            field=models.CharField(max_length=255, verbose_name='tytuł'),
        ),
        migrations.AlterField(
            model_name='training',
            name='jezyk',
            field=models.CharField(blank=True, choices=[('EN', 'Angielski'), ('PL', 'Polski')], max_length=2, null=True, verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='training',
            name='obowiazkowe',
            field=models.BooleanField(default=False, verbose_name='Czy obowiązkowe'),
        ),
    ]