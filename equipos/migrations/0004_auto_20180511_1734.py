# Generated by Django 2.0.5 on 2018-05-11 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0003_auto_20180509_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial_mantenimiento',
            fields=[
                ('id_historial', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('fecha_historial', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id_mantenimiento', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('revisado', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Historial',
        ),
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
        migrations.AddField(
            model_name='mantenimiento',
            name='id_equipos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Equipos'),
        ),
        migrations.AddField(
            model_name='historial_mantenimiento',
            name='id_mantenimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Mantenimiento'),
        ),
    ]
