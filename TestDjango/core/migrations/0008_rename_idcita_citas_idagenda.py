# Generated by Django 3.2.9 on 2021-11-25 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_idagenda_citas_idcita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citas',
            old_name='idcita',
            new_name='idagenda',
        ),
    ]
