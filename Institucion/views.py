from datetime import datetime
from itertools import chain
import json
from xml.dom.minidom import DocumentFragment
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import get_template
from colegiosApp2 import settings
from django.core.files.storage import FileSystemStorage

from Institucion.models import Alumno, Admin, Honorarios, Matriculas, Profesor, Cursos, Tutor
from Institucion.serializers import AlumnoSerializer, AdminSerializer, AdminsGetSerializer, AlumnoTutorSerializer, HonorariosSerializer, MatriculaSerializer, ProfesorSerializer, CursosSerializer, TutorSerializer,AlumnoSerializerWithOutApoderado
from rest_framework import viewsets
# Create your views here.


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matriculas.objects.all()
    serializer_class = MatriculaSerializer

class HonorariosViewSet(viewsets.ModelViewSet):
    queryset = Honorarios.objects.all()
    serializer_class = HonorariosSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

#ALUMNOS
# @csrf_exempt
# def alumnoApi(request, codigoAlumno=0):
#     if request.method == 'GET':
#         alumnos = Alumno.objects.all()
#         alumnos_serializer = AlumnoSerializer(alumnos, many=True)

#         return JsonResponse(alumnos_serializer.data, safe=False)


#     elif request.method == 'POST':
#         alumno_data = JSONParser().parse(request)
#         alumno_serializer = AlumnoSerializer(data = alumno_data)
#         if alumno_serializer.is_valid():
#             alumno_serializer.save()
#             return JsonResponse("Alumno registrado exitosamente!!", safe=False)
#         return JsonResponse(alumno_serializer.errors)
#     elif request.method == 'PUT':
#         alumno_data = JSONParser().parse(request)
#         alumno_before = Alumno.objects.get(codigoAlumno = alumno_data['codigoAlumno'])
#         alumno_serializer = AlumnoSerializer(alumno_before, data = alumno_data)
#         if alumno_serializer.is_valid():
#             alumno_serializer.save()
#             return JsonResponse("Datos del alumno actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del alumno", safe=False)
#     elif request.method == 'DELETE':
#         alumno = Alumno.objects.get(codigoAlumno=codigoAlumno)
#         alumno.delete()
#         return JsonResponse("Alumno eliminado exitosamente!!", safe=False)

# #USUARIOS ADMIN
# @csrf_exempt
# def adminApi(request, id=0):
#     if request.method == 'GET':
#         admins = Admin.objects.all()
#         admin_serializer = AdminsGetSerializer(admins, many=True)
#         return JsonResponse(admin_serializer.data, safe=False)
#     elif request.method == 'POST':
#         admin_data = JSONParser().parse(request)
#         admin_serializer = AdminSerializer(data = admin_data)
#         if admin_serializer.is_valid():
#             admin_serializer.save()
#             return JsonResponse("Usuario registrado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar el usuario", safe=False)
#     elif request.method == 'PUT':
#         admin_data = JSONParser().parse(request)
#         admin_before = Admin.objects.get(id = admin_data['id'])
#         admin_serializer = AdminSerializer(admin_before, data = admin_data)
#         if admin_serializer.is_valid():
#             admin_serializer.save()
#             return JsonResponse("Datos del usuario actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del usuario", safe=False)
#     elif request.method == 'DELETE':
#         admin = Admin.objects.get(id=id)
#         admin.delete()
#         return JsonResponse("Usuario eliminado exitosamente!!", safe=False)

# #PROFESORES
# @csrf_exempt
# def profesorApi(request, codigoProfesor=0):
#     if request.method == 'GET':
#         profesores = Profesor.objects.all()
#         profesor_serializer = ProfesorSerializer(profesores, many=True)
#         return JsonResponse(profesor_serializer.data, safe=False)
#     elif request.method == 'POST':
#         profesor_data = JSONParser().parse(request)
#         profesor_serializer = ProfesorSerializer(data = profesor_data)
#         if profesor_serializer.is_valid():
#             profesor_serializer.save()
#             return JsonResponse("Profesor registrado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar el profesor", safe=False)
#     elif request.method == 'PUT':
#         profesor_data = JSONParser().parse(request)
#         profesor_before = Profesor.objects.get(codigoProfesor = profesor_data['codigoProfesor'])
#         profesor_serializer = ProfesorSerializer(profesor_before, data = profesor_data)
#         if profesor_serializer.is_valid():
#             profesor_serializer.save()
#             return JsonResponse("Datos del profesor actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del profesor", safe=False)
#     elif request.method == 'DELETE':
#         profesor = Profesor.objects.get(codigoProfesor=codigoProfesor)
#         profesor.delete()
#         return JsonResponse("Profesor eliminado exitosamente!!", safe=False)

# #CURSOS
# @csrf_exempt
# def cursosApi(request, codigoCurso=0):
#     if request.method == 'GET':
#         cursos = Cursos.objects.all()
#         curso_serializer = CursosSerializer(cursos, many=True)
#         return JsonResponse(curso_serializer.data, safe=False)
#     elif request.method == 'POST':
#         curso_data = JSONParser().parse(request)
#         curso_serializer = CursosSerializer(data = curso_data, many=True)
#         print(curso_serializer);
#         if curso_serializer.is_valid():
#             curso_serializer.save()
#             return JsonResponse("Curso agregado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar el curso")
#     elif request.method == 'PUT':
#         curso_data = JSONParser().parse(request)
#         curso_before = Cursos.objects.get(codigoCurso = curso_data['codigoCurso'])
#         curso_serializer = CursosSerializer(curso_before, data = curso_data)
#         if curso_serializer.is_valid():
#             curso_serializer.save()
#             return JsonResponse("Datos del curso actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del profesor", safe=False)
#     elif request.method == 'DELETE':
#         curso = Cursos.objects.get(codigoCurso=codigoCurso)
#         curso.delete()
#         return JsonResponse("Curso eliminado exitosamente!!", safe=False)

@csrf_exempt
def detailApi(request):
    if request.method == 'GET':
        
        list_precios_cursos = Cursos.objects.values_list('precio', flat=True)
        list_honorarios_profesores = Honorarios.objects.values_list('monto', flat=True)
        resp_data = {'cantidadCursos': len(Cursos.objects.all()), 
                     'cantidadAlumnos': len(Alumno.objects.all()),
                     'cantidadPadres': len(Tutor.objects.all()),
                     'cantidadProfesores': len(Profesor.objects.all()),
                     'montoTotalCursos': sum(list_precios_cursos),
                     'montoTotalHonorariosProfesores': sum(list_honorarios_profesores)
                     }
        return JsonResponse(resp_data)

@csrf_exempt
def loginAdminApi(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            result = Admin.objects.get(usuario=data['usuario'], password=data['password'])
            res = AdminSerializer(result, many=False)
            return JsonResponse({"mensaje": 'Bienvenido ' + res.data['nombres'], "nombres": res.data['nombres']}, status=200)
        except Admin.DoesNotExist:
            return JsonResponse({"mensaje": "Usuario invalido!!"}, status=404)
        #resp_data = {'cantidadCursos': 1 }

@csrf_exempt
def misCursosApi(request):
    if request.method == 'GET':
        try:
            cursos = Matriculas.objects.filter(codigoAlumno = request.GET['codigoAlumno'])
            print("CURSOS")
            curso_serializer = MatriculaSerializer(cursos, many=True)
            print(curso_serializer)
            return JsonResponse(curso_serializer.data, safe=False)
        except Cursos.DoesNotExist:
            return JsonResponse("El usuario no cuenta con cursos registrados", safe=False)
        #resp_data = {'cantidadCursos': 1 }

@csrf_exempt
def misCursosAsignadosApi(request):
    if request.method == 'GET':
        try:
            cursos = Cursos.objects.filter(codigoProfesor = request.GET['codigoProfesor'])
            curso_serializer = CursosSerializer(cursos, many=True)
            return JsonResponse(curso_serializer.data, safe=False)
        except Cursos.DoesNotExist:
            return JsonResponse("El docente no cuenta con cursos asignados", safe=False)

@csrf_exempt
def misHonorarios(request):
    if request.method == 'GET':
        try:
            honorarios = Honorarios.objects.filter(codigoProfesor = request.GET['codigoProfesor'])
            honorarios_serializer = HonorariosSerializer(honorarios, many=True)
            return JsonResponse(honorarios_serializer.data, safe=False)
        except Honorarios.DoesNotExist:
            return JsonResponse("El docente no cuenta con honorarios", safe=False)

@csrf_exempt
def misHijosApi(request):
    if request.method == 'GET':
        try:
            alumnos = Alumno.objects.filter(codigoTutor = request.GET['codigoApoderado'])
            alumnos_serializer = AlumnoTutorSerializer(alumnos, many=True)
            return JsonResponse(alumnos_serializer.data, safe=False)
        except Alumno.DoesNotExist:
            return JsonResponse("El usuario no cuenta con hijos registrados", safe=False)
        #resp_data = {'cantidadCursos': 1 }

@csrf_exempt
def loginAlunmo(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            result = Alumno.objects.get(correo=data['correo'], password=data['password'])
            res = AlumnoSerializer(result, many=False)
            print(res['alumnoVerificado'].value)
            if(res['alumnoVerificado'].value == True):
                return JsonResponse({"mensaje": 'Bienvenido ' + res.data['nombres'], "nombres": res.data['nombres'], "codigoAlumno": res.data['codigoAlumno']}, status=200)
            else:
                return JsonResponse({"mensaje": "Hola "+ res['nombres'].value+", tu usuario aun no fue confirmado por el administrador"}, status=400)
        except Alumno.DoesNotExist:
            return JsonResponse({"mensaje": "Usuario invalido!!"}, status=404)
        #resp_data = {'cantidadCursos': 1 }

@csrf_exempt
def loginApoderado(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            result = Tutor.objects.get(numDocumento=data['usuario'])
            res = TutorSerializer(result, many=False)
            if(res['numDocumento'].value == data['password']):
                return JsonResponse({"mensaje": 'Bienvenido ' + res.data['nombres'], "nombres": res.data['nombres'], "codigoTutor": res.data['codigoTutor']}, status=200)
            else:
                return JsonResponse({"mensaje": "Usuario invalido!!"}, status=400)
        except Tutor.DoesNotExist:
            return JsonResponse({"mensaje": "Usuario invalido!!"}, status=404)
        #resp_data = {'cantidadCursos': 1 }


@csrf_exempt
def loginDocente(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            result = Profesor.objects.get(numDocumento=data['usuario'])
            res = ProfesorSerializer(result, many=False)
            if(res['numDocumento'].value == data['password']):
                return JsonResponse({"mensaje": 'Bienvenido ' + res.data['nombres'], "nombres": res.data['nombres'], "codigoProfesor": res.data['codigoProfesor']}, status=200)
            else:
                return JsonResponse({"mensaje": "Usuario invalido!!"}, status=400)
        except Profesor.DoesNotExist:
            return JsonResponse({"mensaje": "Usuario invalido!!"}, status=404)
# @csrf_exempt
# def loginAlunmo(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         try:
#             result = Alumno.objects.get(correo=data['usuario'], password=data['password'])
#             if(data['usuario'] == data['password']):
#                 res = AlumnoSerializer(result, many=False)
#                 return JsonResponse({"mensaje": 'Bienvenido ' + res.data['nombres'], "nombres": res.data['nombres']}, status=200)
#             else:
#                 return JsonResponse({"mensaje": "Usuario invalido"}, status=400)
#         except Admin.DoesNotExist:
#             return JsonResponse({"mensaje": "Usuario invalido!!"}, status=404)
#         #resp_data = {'cantidadCursos': 1 }

@csrf_exempt
def alumnoRegister(request):
    if request.method == 'POST':
        alumno_data = JSONParser().parse(request)
        alumno_serializer = AlumnoSerializerWithOutApoderado(data = alumno_data)
        if alumno_serializer.is_valid():
            alumno_serializer.save()
            template = get_template('template-email.html')
            content = template.render({'nombres': alumno_data['nombres']})
            msg = EmailMultiAlternatives(
                'Gracias por registrarte en Centro de Tareas y Reforzamiento Los Álamos',
                'Hola, te enviamos un correo por tu registro',
                '-==CentrosAPP (UNSA)==-',
                [alumno_data['correo']]
            )
            msg.attach_alternative(content, 'text/html')
            msg.send()
            
            return JsonResponse("Alumno registrado exitosamente!!", safe=False)
        return JsonResponse(alumno_serializer.errors, status=404)


@csrf_exempt
def uploadImageAlumno(request):
    if request.method == 'POST':
        try:
            user = Alumno.objects.get(codigoAlumno=request.POST.get('codigoAlumno'))
            upload = request.FILES['imagen']
            fss = FileSystemStorage(location='media/alumnos/')
            file = fss.save(upload.name, upload)
            # file_url = fss.url(file)
            user.imagen = 'alumnos/'+upload.name
            user.save()
            return JsonResponse("Imagen del alumno actualizado exitosamente!!", safe=False)
        except Alumno.DoesNotExist:
            return JsonResponse("Error al actualizar la imagen del alumno", safe=False)

@csrf_exempt
def uploadImageApoderado(request):
    if request.method == 'POST':
        try:
            user = Tutor.objects.get(codigoTutor=request.POST.get('codigoTutor'))
            upload = request.FILES['imagen']
            fss = FileSystemStorage(location='media/apoderado/')
            file = fss.save(upload.name, upload)
            # file_url = fss.url(file)
            user.imagen = 'apoderado/'+upload.name
            user.save()
            return JsonResponse("Imagen del apoderado actualizado exitosamente!!", safe=False)
        except Tutor.DoesNotExist:
            return JsonResponse("Error al actualizar la imagen del apoderado", safe=False)

@csrf_exempt
def uploadImageDocente(request):
    if request.method == 'POST':
        try:
            user = Profesor.objects.get(codigoProfesor=request.POST.get('codigoProfesor'))
            upload = request.FILES['imagen']
            fss = FileSystemStorage(location='media/docentes/')
            file = fss.save(upload.name, upload)
            # file_url = fss.url(file)
            user.imagen = 'docentes/'+upload.name
            user.save()
            return JsonResponse("Imagen del docente actualizado exitosamente!!", safe=False)
        except Profesor.DoesNotExist:
            return JsonResponse("Error al actualizar la imagen del docente", safe=False)