from django.urls import re_path
from Institucion import views
from Institucion.routers import router

urlpatterns = [
     re_path(r'^misHonorarios$', views.misHonorarios, name="misHonorarios"),
    re_path(r'^misCursos$', views.misCursosApi, name="misCursos"),
    re_path(r'^misCursosAsignados$', views.misCursosAsignadosApi, name="misCursosAsignados"),
    re_path(r'^uploadImagenAlumno$', views.uploadImageAlumno, name="uploadImagenAlumno"),
    re_path(r'^uploadImagenApoderado$', views.uploadImageApoderado, name="uploadImagenApoderado"),
    re_path(r'^uploadImagenDocente$', views.uploadImageDocente, name="uploadImagenDocente"),
    re_path(r'^loginAdmin$', views.loginAdminApi, name="loginAdmin"),
    re_path(r'^loginAlumno$', views.loginAlunmo, name="loginAlumno"),
    re_path(r'^loginApoderado$', views.loginApoderado, name="loginApoderado"),
    re_path(r'^loginDocente$', views.loginDocente, name="loginDocente"),
    re_path(r'^detail$', views.detailApi, name="detail"),
    re_path(r'^alumnoRegister$', views.alumnoRegister, name="alumnoRegister"),
    re_path(r'^misHijos$', views.misHijosApi, name="misHijos"),
    # re_path(r'^profesores$', views.profesorApi, name="profesor"),
    # re_path(r'^profesores/([0-9]+)$', views.profesorApi),
    # re_path(r'^cursos$', views.cursosApi, name="curso"),
    # re_path(r'^cursos/([0-9]+)$', views.cursosApi),
    # re_path(r'^alumnos/$', views.alumnoApi, name="alumno"),
    # re_path(r'^alumnos/([0-9]+)$', views.alumnoApi),
    # re_path(r'^admin$', views.adminApi, name="admin"),
    # re_path(r'^admin/([0-9]+)$', views.adminApi)
]

urlpatterns += router.urls