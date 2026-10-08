from django.db import models
from .choices import Estado
from localflavor.br.models import BRCPFField

class Client (models.Model):
    name = models.CharField('Nome Completo', max_length=100)
    cpf = BRCPFField('CPF', unique=True)
    birth_date = models.DateField('Data de Nascimento')
    address = models.CharField('Endereço', max_length=100)
    number = models.CharField('Nº', max_length=7, blank=True)
    neighborhood = models.CharField('Bairro', max_length=100)
    zip_code = models.CharField('CEP', max_length=10)
    city = models.CharField('Município', max_length=100)
    state = models.CharField('UF', max_length=2, choices=Estado.choices, default=Estado.AL)
    phone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.name


class Number (models.Model):
    card = models.IntegerField(verbose_name='Nº do Cartão', max_length=3, blank=False),

    def __str__(self):
        return self.card