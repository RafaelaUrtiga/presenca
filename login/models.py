from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
        # esse é um usuário mais básico, nao tem muita funcionalidade
from django.contrib.auth.models import AbstractUser, BaseUserManager


### gerenciador da criação dos usuários ####

class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    #### funções de validação para tipo de usuário #####

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True) # Não é sugerido o uso ao acesso admin do django
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField ('E-mail', unique=True)
    fone = models.CharField ('Telefone', max_length=15)
    is_staff = models.BooleanField ('Membro da equipe', default=True)

    USERNAME_FIELD = 'email' # campo que faz login junto com a senha, mas poderia ser nome, cpf...
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone'] # email e password nao foi colocado pois o próprio sistema já solicita, pois está na autenticação

    def __str__(self):
        return self.email

    objects = UsuarioManager()  # os objetos desse model são gerenciados pelo UsuarioManager, tem que dizer senão volta para o padrão Django

###### 3ª forma de criar uruário ######

"""from django.contrib.auth import get_user_model

class Post(models.Model):
    usuario = models.ForeignKey(get_user_model(), verbose_name = "Usuário", on_delete=models.CASCADE)
    titulo = models.CharField('Titulo')

    def __str__(self):
        return self.titulo"""

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