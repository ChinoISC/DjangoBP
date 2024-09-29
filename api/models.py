from django.db import models

class Usuario(models.Model):
    # ID del usuario, se autoincrementa y es la clave primaria
    usuarios_id = models.AutoField(db_column="ID", primary_key=True)
    
    # Campo para almacenar el nombre completo del usuario, con un máximo de 255 caracteres
    nombre_completo = models.CharField(max_length=255)
    
    # Campo para almacenar el correo electrónico del usuario, debe ser único
    correo_electronico = models.EmailField(unique=True)

    class Meta:
        # Nombre de la tabla en la base de datos
        db_table = "usuarios"


class Genero(models.Model):
    # ID del género, se autoincrementa y es la clave primaria
    genero_id = models.AutoField(db_column="ID", primary_key=True)
    
    # Campo para almacenar el nombre del género, con un máximo de 255 caracteres
    nombre = models.CharField(max_length=255)

    class Meta:
        # Nombre de la tabla en la base de datos
        db_table = "generos"
