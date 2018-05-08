# Generated by Django 2.0.4 on 2018-04-29 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id_equipos', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(blank=True, max_length=20, null=True)),
                ('funcionario', models.CharField(blank=True, max_length=45, null=True)),
                ('cuenta_usuario', models.CharField(blank=True, max_length=20, null=True)),
                ('contrasena', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion_ip', models.GenericIPAddressField()),
                ('id_Departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id_hardware', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('hardware', models.CharField(blank=True, max_length=20, null=True)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('serial', models.CharField(blank=True, max_length=25, null=True)),
                ('id_equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Equipos')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id_historial', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('historial', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField()),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modelos',
            fields=[
                ('id_modelo', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('modelo', models.CharField(blank=True, max_length=20, null=True)),
                ('id_equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Equipos')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id_software', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('fecha_instalacion', models.DateTimeField()),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('licencia', models.CharField(blank=True, max_length=25, null=True)),
                ('tipo_licencia', models.CharField(blank=True, max_length=45, null=True)),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Equipos')),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_Equipos',
            fields=[
                ('id_tipos_equipos', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='equipos',
            name='id_Tipos_Equipos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Tipos_Equipos'),
        ),
    ]
