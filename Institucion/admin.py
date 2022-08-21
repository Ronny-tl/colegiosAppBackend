from django.contrib import admin

from Institucion.models import Alumno, Profesor, Cursos, Admin, Matriculas, Honorarios, Tutor
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Cursos)
admin.site.register(Admin)
admin.site.register(Matriculas)
admin.site.register(Honorarios)
admin.site.register(Tutor)