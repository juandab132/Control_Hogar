from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Usuario(models.Model):
    identifier = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=45)
    telefono = models.CharField(max_length=15)
    telefonoEmergencia = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.identifier}"

class Camera(models.Model):
    identifier = models.CharField(max_length=45)
    status = models.BooleanField("Is Active")
    video = models.URLField()
    number = models.IntegerField()

    def __str__(self):
        return f" {self.identifier}"

class Light(models.Model):
    identifier = models.CharField(max_length=45)
    status = models.BooleanField(default=False)
    room = models.CharField(max_length=45)
    num = models.IntegerField()
    def __str__(self):
        return f" {self.identifier}"