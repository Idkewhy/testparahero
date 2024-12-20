# Generated by Django 3.2.25 on 2024-11-01 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201124_0614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['apellido_paterno', 'apellido_materno', 'nombres']},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='firstname',
            new_name='apellido_materno',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='surname',
            new_name='apellido_paterno',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='current_class',
            new_name='curso_actual',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='date_of_admission',
            new_name='fecha_admision',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='date_of_birth',
            new_name='fecha_nacimiento',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='other_name',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='others',
            new_name='observaciones',
        ),
        migrations.RemoveField(
            model_name='student',
            name='current_status',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_mobile_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='student',
            name='registration_number',
        ),
        migrations.AddField(
            model_name='student',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='foto',
            field=models.ImageField(blank=True, upload_to='students/fotos/'),
        ),
        migrations.AddField(
            model_name='student',
            name='rut',
            field=models.CharField(blank=True, max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message="El RUT debe estar en el formato 'XXXXXXXX-X'", regex='^\\d{1,2}\\d{3}\\d{3}-[0-9kK]{1}$')]),
        ),
        migrations.AddField(
            model_name='student',
            name='sexo',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], default='masculino', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='telefono_apoderado',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='El número de teléfono no tiene el formato correcto.', regex='^[0-9]{9,15}$')]),
        ),
    ]
