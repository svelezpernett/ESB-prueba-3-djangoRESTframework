# Generated by Django 4.0.5 on 2022-06-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESB_api', '0005_alter_clientes_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]
