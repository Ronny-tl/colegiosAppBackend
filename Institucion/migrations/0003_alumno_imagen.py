# Generated by Django 4.0.4 on 2022-08-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institucion', '0002_alter_alumno_codigotutor_alter_tutor_apellidos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='imagen',
            field=models.ImageField(null=True, upload_to='alumnos'),
        ),
    ]
