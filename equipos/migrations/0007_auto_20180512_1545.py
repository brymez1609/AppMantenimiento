# Generated by Django 2.0.5 on 2018-05-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0006_auto_20180512_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimiento',
            name='fecha',
            field=models.DateField(),
        ),
    ]
