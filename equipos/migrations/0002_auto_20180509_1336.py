# Generated by Django 2.0.5 on 2018-05-09 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='id_Departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ubicacion.Departamento'),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='id_Tipos_Equipos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='equipos.Tipos_Equipos'),
        ),
    ]
