# Generated by Django 4.0.5 on 2022-06-15 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ESB_api', '0010_alter_factura_id_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='hora',
            new_name='fecha_hora',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='fecha',
        ),
    ]