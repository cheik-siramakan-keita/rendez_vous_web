# Generated by Django 2.2.1 on 2019-10-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous_web', '0012_auto_20191010_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creneau',
            name='selection',
            field=models.BooleanField(default=False),
        ),
    ]
