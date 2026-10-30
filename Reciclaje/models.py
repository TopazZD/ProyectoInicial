from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    comuna = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.usuario.username 