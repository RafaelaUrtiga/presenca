from django.contrib import admin

from .models import User, Client

class ClientAdmin(admin.ModelAdmin): #display com o que eu quiser na área de admin
    list_display = ('nome', 'sobrenome', 'telefone')

admin.site.register(User),
admin.site.register(Client, ClientAdmin),
