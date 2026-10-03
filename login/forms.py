from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario


##### criação do usuário ####

class CustomUsuarioCriateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone') # colocamos o que tem no campo required do model
        labels = {'username': 'Username/E-mail'}


    #### subscreve o método save para que o usuario seja setado para o email ####

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"]) # validação dos 2 campos de senha e criptografar
        user.email = self.cleaned_data['username'] # colocando o email no username

        if commit:
            user.save()
        return user


##### alteração do usuário ####

class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')