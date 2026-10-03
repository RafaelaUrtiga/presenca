from django.contrib import admin
# from .models import Post
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCriateForm, CustomUsuarioChangeForm
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCriateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
    )


#### uso do admin pelo padrão Django ######

"""@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_usuario')
    exclude = ['usuario',] # o dropdown do autor some, para que um usuario nao use o nome de outro

    def _usuario(self, instance): # para visualizar o nome completo
        return f'{instance.usuario.get_full_name()}'

    def get_queryset(self, request): # função que consulta o banco de dados
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(usuario=request.user)

    def save_model(self, request, obj, form, change): # subescrevendo o método de salvar para incluir apenas o usuário logado
        obj.usuario = request.user # coloca o usuário logado
        super().save_model(request, obj, form, change) # altera o save"""