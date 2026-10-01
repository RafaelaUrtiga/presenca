from django.db import models

###### 3ª forma de criar uruário ######

from django.contrib.auth import get_user_model

class Post(models.Model):
    usuario = models.ForeignKey(get_user_model(), verbose_name = "Usuário", on_delete=models.CASCADE)
    titulo = models.CharField('Titulo')

    def __str__(self):
        return self.titulo

###### 2ª forma de criar um usuário #####

"""
from django.conf import settings

class Post(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = "Usuário", on_delete=models.CASCADE) # veio do settings
    titulo = models.CharField('Titulo')

    def __str__(self):
        return self.titulo"""

###### 1ª forma de criação de usuario, com o modelo do próprio django ######
""" 
 from django.contrib.auth.models import User

class Post(models.Model):
    usuario = models.ForeignKey(User, verbose_name = "Usuário", on_delete=models.CASCADE)
    titulo = models.CharField('Titulo')

    def __str__(self):
        return self.titulo """