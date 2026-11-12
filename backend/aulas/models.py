from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mostrar = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Materia(models.Model):
    nombre = models.CharField(max_length=128)
    cant_alumnos = models.IntegerField(default=5)

    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.PROTECT,
        db_column="id_carrera"
    )

    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.PROTECT,
        db_column="id_profesor"
    )

    def __str__(self):
        return self.nombre


class Aula(models.Model):
    descripcion = models.CharField(max_length=128)
    ubicacion = models.CharField(max_length=128)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
    
    
class ReservaAula(models.Model):
    aula = models.ForeignKey(
        Aula,
        on_delete=models.PROTECT,
        db_column="id_aula"
    )

    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observacion = models.CharField(max_length=256)

    def __str__(self):
        return f"Reserva del aula {self.aula_id}"


class HorarioMateria(models.Model):
    materia = models.ForeignKey(
        Materia,
        on_delete=models.PROTECT,
        db_column="id_materia"
    )

    reserva = models.ForeignKey(
        ReservaAula,
        on_delete=models.PROTECT,
        db_column="id_reserva"
    )

    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()

    def __str__(self):
        return f"Horario de {self.materia.nombre}"