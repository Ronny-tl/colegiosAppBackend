# Generated by Django 4.0.4 on 2022-08-21 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Institucion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='codigoTutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_tutor', to='Institucion.tutor'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='apellidos',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='nombres',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
