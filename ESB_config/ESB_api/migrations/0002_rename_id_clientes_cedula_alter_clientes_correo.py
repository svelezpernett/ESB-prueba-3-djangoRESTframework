# Generated by Django 4.0.5 on 2022-06-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESB_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='id',
            new_name='cedula',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='correo',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
