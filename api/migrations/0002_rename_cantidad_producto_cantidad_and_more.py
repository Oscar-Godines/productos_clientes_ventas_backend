# Generated by Django 4.1.7 on 2023-02-24 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cantidad',
            new_name='CANTIDAD',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='NOMBRE',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='PRECIO',
        ),
    ]
