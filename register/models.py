from django.db import models
from .choices import Estado
from localflavor.br.models import BRCPFField

class Client (models.Model):
    nome = models.CharField('Nome Completo', max_length=100)
    cpf = BRCPFField('CPF', unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.CharField ('Nº', max_length=7, blank=True)
    bairro = models.CharField('Bairro', max_length=100)
    cep = models.CharField('CEP', max_length=10)
    municipio = models.CharField('Município', max_length=100)
    uf = models.CharField('UF', max_length=2, choices=Estado.choices, default=Estado.AL)
    telefone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.nome
