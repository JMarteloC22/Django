# Generated by Django 5.1.1 on 2024-09-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_conductor', models.CharField(max_length=70)),
                ('edad_empleado', models.CharField(max_length=2)),
                ('licencia', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=70)),
                ('edad_empleado', models.CharField(max_length=2)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=50)),
                ('ganancias', models.CharField(max_length=20)),
                ('impuestos', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('combustible', models.CharField(max_length=30)),
                ('transmision', models.CharField(max_length=30)),
            ],
        ),
    ]
