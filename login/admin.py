from django.contrib import admin
from .models import Post

@admin.register(Post)
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
        super().save_model(request, obj, form, change) # altera o save