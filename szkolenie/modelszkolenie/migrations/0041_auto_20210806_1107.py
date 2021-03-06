# Generated by Django 3.2.6 on 2021-08-06 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelszkolenie', '0040_training_obowiazkowe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='poczatek',
        ),
        migrations.CreateModel(
            name='CompletedTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ukonczenia', models.DateField(blank=True, null=True)),
                ('osoba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelszkolenie.user')),
                ('szkolenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelszkolenie.training')),
            ],
        ),
    ]
