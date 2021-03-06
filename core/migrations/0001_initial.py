# Generated by Django 3.2.4 on 2021-07-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='RUT')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=40, verbose_name='Direccion')),
                ('correo', models.CharField(max_length=40, verbose_name='Email')),
                ('pais', models.CharField(max_length=40, verbose_name='Pais')),
                ('contraseña', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contraseña')),
            ],
        ),
    ]
