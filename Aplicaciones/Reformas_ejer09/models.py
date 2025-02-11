from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    foto = models.ImageField(upload_to='clientes/', null=True, blank=True)  # Nuevo campo de foto


class Vivienda(models.Model):
    id_vivienda = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='viviendas')
    foto = models.ImageField(upload_to='viviendas/', null=True, blank=True)  # Aquí agregamos el campo foto


class ProyectoDeReforma(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    id_vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name='proyectos')
    descripcion = models.TextField()  # Descripción del proyecto de reforma
    fecha_inicio = models.DateField()  # Fecha de inicio de la reforma
    fecha_fin = models.DateField()  # Fecha de fin de la reforma
    estado = models.CharField(
        max_length=20,
        choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('Finalizado', 'Finalizado')],
        default='Pendiente'
    )  # Estado del proyecto



class Material(models.Model):
    id_material = models.AutoField(primary_key=True)  # Identificador único
    id_proyecto = models.ForeignKey(ProyectoDeReforma, on_delete=models.CASCADE, related_name='materiales')  # Relación con ProyectoDeReforma
    nombre_material = models.CharField(max_length=255)  # Nombre del material
    cantidad = models.IntegerField()