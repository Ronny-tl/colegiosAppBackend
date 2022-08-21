from rest_framework.routers import DefaultRouter
from Institucion.views import AdminViewSet, AlumnoViewSet, CursoViewSet, HonorariosViewSet, MatriculaViewSet, ProfesorViewSet, TutorViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')
router.register(r'admin', AdminViewSet, basename='admin')
router.register(r'docentes', ProfesorViewSet, basename='docentes')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'pagos', MatriculaViewSet, basename='pagos')
router.register(r'honorarios', HonorariosViewSet, basename='honorarios')
router.register(r'tutor', TutorViewSet, basename='tutor')