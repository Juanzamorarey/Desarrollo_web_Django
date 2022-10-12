from django.db import models

# Create your models here.

# Aquí tenemos los modelos que después serán utilizados como BBDD en nuestra app. 
# Charfiled -> Campo de string
# PositiveSmallIntegerFiled -> Integer pequeño
# DateField -> Fecha. Si se añade el campo auto_now_add se agrega automáticamente el momento y día en el que se añaden registros a la tabla.
# atributo choices en CharField -> Indica la existencia de una serie de posibilidades. Toma como argumento una lista 
# ForeignKey indica las dependencias entre las tablas de la BBDD, en este caso un estudiante pertenece a una carrera. El campo no puede ser null, ni estar en blanco y
# por último el on_delete hace que se eliminen en cascada, es decir que en caso de borrarse una carrera se borrarán todos los estudiantes que pertenezcan a dicha carrera.
# BooleanField -> Valor booleano, solo acepta true o False.
# AutoField -> Indica un valor autoincremental de tipo integer.


class Carrera(models.Model):
    codigo = models.CharField(max_length=3,primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = f"{self.nombre} (Duración: {self.duracion} año(s))"
        # return txt.format(self.nombre, self.duracion)
        return txt

class Estudiante(models.Model):
    dni = models.CharField(max_length=8,primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [("F","Femenino"),("M","Masculino")]
    sexo = models.CharField(max_length=1,choices=sexos)
    carrera = models.ForeignKey(Carrera, null= False, blank = False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def Nombre_Completo(self):
        # Este método de la clase nos devuleve un string partiendo del propio objeto de la clase
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        txt = f"{self.nombres} {self.apellidoPaterno} {self.apellidoMaterno} ({self.dni})"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        return txt

class Curso(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = f"{self.docente} {self.nombre} ({self.codigo})"
        return txt

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = f"{self.estudiante} {self.curso}"
        return txt