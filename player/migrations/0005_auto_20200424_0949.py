# Generated by Django 3.0.5 on 2020-04-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_pom_pom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Middle name'),
        ),
    ]
