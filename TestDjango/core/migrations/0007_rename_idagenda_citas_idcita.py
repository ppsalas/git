# Generated by Django 3.2.9 on 2021-11-25 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211125_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citas',
            old_name='idagenda',
            new_name='idcita',
        ),
    ]
