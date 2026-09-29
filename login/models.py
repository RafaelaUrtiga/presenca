from django.db import models

class User (models.Model):
    nome = models.CharField('Nome Completo', max_length=100),
    email = models.EmailField('E-mail', max_length=100),
    telefone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.nome

class Client (models.Model):
    nome = models.CharField('Nome', max_length=100),
    sobrenome = models.CharField('Sobrenome', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'