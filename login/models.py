from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    usuario = models.ForeignKey(User, verbose_name = "Usuário", on_delete=models.CASCADE)
    titulo = models.CharField('Titulo')

    def __str__(self):
        return self.titulo