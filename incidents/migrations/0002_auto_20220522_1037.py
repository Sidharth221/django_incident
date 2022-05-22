# Generated by Django 3.2.9 on 2022-05-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='submitted',
        ),
        migrations.AlterField(
            model_name='incident',
            name='type_env',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='type_inju',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='type_property',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='type_vehicle',
            field=models.BooleanField(default=False),
        ),
    ]
