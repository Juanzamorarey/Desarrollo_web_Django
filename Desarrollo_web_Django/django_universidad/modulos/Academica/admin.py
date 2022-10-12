from django.contrib import admin

from modulos.Academica.models import Carrera, Curso, Matricula, Estudiante

# Register your models here.
# Hay que importar los modulos de la manera correcta como se ve en la linea 3 y luego registrarlos como se ve en las sigueinte líneas admin.site.register(nombre claseimportadaarriba)

admin.site.register(Carrera) 
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)
