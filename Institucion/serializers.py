from dataclasses import field, fields
from rest_framework import serializers
from Institucion.models import Alumno, Admin, Tutor, Profesor, Cursos, Matriculas, Honorarios

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tutor
        fields='__all__'
        
class AlumnoSerializer(serializers.ModelSerializer):
    default=[]
    class Meta:
        model=Alumno
        fields='__all__'
    def to_representation(self, instance):
        return {
            'codigoAlumno': instance.codigoAlumno,
            'nombres': instance.nombres,
            'apellidos': instance.apellidos,
            'direccion': instance.direccion,
            'telefono': instance.telefono,
            'tipoDocumento': instance.tipoDocumento,
            'numDocumento': instance.numDocumento,
            'nombresTutor': instance.codigoTutor.nombres if instance.codigoTutor else "",
            'codigoTutor': instance.codigoTutor.codigoTutor if instance.codigoTutor else "",
            'fechaNacimiento': instance.fechaNacimiento,
            'correo': instance.correo,
            'alumnoVerificado': instance.alumnoVerificado
        }

class AlumnoSerializerWithOutApoderado(serializers.ModelSerializer):
    class Meta:
        model=Alumno
        fields=('nombres', 'apellidos', 'direccion', 'telefono', 'tipoDocumento', 'numDocumento', 'fechaNacimiento', 'correo', 'password', 'alumnoVerificado')
    def to_representation(self, instance):
        return {
            'codigoAlumno': instance.codigoAlumno,
            'nombres': instance.nombres,
            'apellidos': instance.apellidos,
            'direccion': instance.direccion,
            'telefono': instance.telefono,
            'tipoDocumento': instance.tipoDocumento,
            'numDocumento': instance.numDocumento,
            'fechaNacimiento': instance.fechaNacimiento,
            'email': instance.email,
            'alumnoVerificado': instance.alumnoVerificado
        }

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields='__all__'
        #fields=('id', 'usuario', 'password', 'nombres', 'apellidos', 'tipoUsuario')

class AdminsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('id', 'usuario', 'nombres', 'apellidos', 'tipoUsuario')

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profesor
        fields='__all__'

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cursos
        fields='__all__'
    def to_representation(self, instance):
        return {
            'codigoCurso': instance.codigoCurso,
            'nombre': instance.nombre,
            'precio': instance.precio,
            'fechaInicio': instance.fechaInicio,
            'fechaFin': instance.fechaFin,
            'nombreProfesor': instance.codigoProfesor.nombres,
            'apellidoProfesor': instance.codigoProfesor.apellidos,
            'codigoProfesor': instance.codigoProfesor.codigoProfesor,
        }

class HonorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Honorarios
        fields='__all__'
    def to_representation(self, instance):
        return {
            'codigoHonorario': instance.codigoHonorario,
            'descripcion': instance.descripcion,
            'monto': instance.monto,
            'codigoProfesor': instance.codigoProfesor.codigoProfesor,
            'nombresProfesor': instance.codigoProfesor.nombres,
            'apellidosProfesor': instance.codigoProfesor.apellidos
        }

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Matriculas
        fields='__all__'
    def to_representation(self, instance):
        return {
            'codigoRegistro': instance.codigoRegistro,
            'descripcion': instance.descripcion,
            'codigoAlumno': instance.codigoAlumno.codigoAlumno,
            'nombresAlumno': instance.codigoAlumno.nombres,
            'apellidosAlumno': instance.codigoAlumno.apellidos,
            'codigoCurso': instance.codigoCurso.codigoCurso,
            'nombreCurso': instance.codigoCurso.nombre,
            'codigoProfesor': instance.codigoCurso.codigoProfesor.codigoProfesor,
            'nombresProfesor': instance.codigoCurso.codigoProfesor.nombres,
            'apellidosProfesor': instance.codigoCurso.codigoProfesor.apellidos,
            'precioCurso': instance.codigoCurso.precio,
            'monto': instance.monto
        }
