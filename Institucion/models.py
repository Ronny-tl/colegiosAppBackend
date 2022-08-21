from operator import mod
from django.db import models

# Create your models here.
class Tutor(models.Model):
    codigoTutor = models.AutoField(primary_key=True, blank=True)
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)


    # def nombre_completo(self):
    #     return "{}, {}".format(self.apellidos, self.nombres)

    def __str__(self):
        return {'nombres': self.nombres, 'codigoTutor': self.codigoTutor}

    def get_internal_type(self):
      return {'nombres': 'sin Apoderado', 'codigoTutor': 'sin Apoderado'}

class Alumno(models.Model):
    codigoAlumno = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    codigoTutor = models.ForeignKey(Tutor, related_name='fk_tutor', on_delete=models.CASCADE, null=True, blank=True)
    correo = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    alumnoVerificado = models.BooleanField()

    # def nombre_completo(self):
    #     return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return {'nombres': self.nombres, 'apellidos':self.apellidos, 'codigoAlumno': self.codigoAlumno}

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoUsuario = models.CharField(max_length=100)
    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()


class Profesor(models.Model):
    codigoProfesor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)

    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return {'nombres': self.nombres, 'apellidos':self.apellidos, 'codigoProfesor': self.codigoProfesor}

class Cursos(models.Model):
    codigoCurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits = 7, decimal_places = 2)
    codigoProfesor = models.ForeignKey(Profesor, related_name='fk_profesor',blank=True, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

    def __str__(self):
        return {'nombre': self.nombres, 'precio':self.apellidos, 'codigoCurso': self.codigoCurso}

class Matriculas(models.Model):
    codigoRegistro = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    codigoAlumno = models.ForeignKey(Alumno, related_name='fk_alumno_pagos', on_delete=models.CASCADE)
    codigoCurso = models.ForeignKey(Cursos, related_name='fk_cursos', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits = 7, decimal_places = 2)

class Honorarios(models.Model):
    codigoHonorario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    codigoProfesor = models.ForeignKey(Profesor, related_name='fk_profesor_h', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits = 7, decimal_places = 2)
    
    # def detalle(self):
    #     return "{} - {}".format(self.codigoProfesor, self.monto)
    # def __str__(self):
    #     return self.detalle()
    def __str__(self):
        return {'descripcion': self.descripcion, 'monto':self.monto, 'codigoHonorario': self.codigoHonorario, 'codigoProfesor': self.codigoProfesor}