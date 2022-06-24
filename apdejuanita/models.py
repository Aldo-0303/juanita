from django.db import models

# Create your models here.

class persona(models.Model):
    id_persana = models.AutoField(primary_key=True),
    nonbre_persona = models.CharField(max_length=50)

