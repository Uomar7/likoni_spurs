# Generated by Django 3.0.5 on 2020-04-23 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='dob',
            new_name='_dob',
        ),
    ]
