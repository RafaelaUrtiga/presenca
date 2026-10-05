import re
from django.utils import timezone
from .models import Client
from django import forms

#### Remove o que não for número
#### criar as mascaras
# fazer o altopreenchimento
# regra co cep
# regra do cpf
 
def digitos(valor):
    return re.sub(r'\D', '', valor or '')


class ClientForm(forms.ModelForm):
    cep = forms.Charfield(label='CEP')

    class Meta:
        model = Client
        fields = [
            'nome', 'cpf', 'data_nascimento', 'telefone', 'cep', 'endereco', 'numero', 'bairro', 'municipio', 'uf'
        ]
        widgets={
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00', 'inputmode': 'numeric'}),
            'cep': forms.TextInput(attrs={'placeholder':'00.000-00', 'inputmode': 'numeric'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 00000-0000', 'inputmode': 'numeric'}),
            'numero': forms.TextInput(attrs={'placeholder': 's/n'}),
            'data_nascimento': forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'),
        }

    ## mantem o nome com apenas 1 espaço
    def clean_nome(self):
        return ' '.join(self.cleaned_data['nome'].split())

    ##remove a mascara para guardar os 11 dígitos
    def clean_cpf(self):
        return digitos(self.cleaned_data['cpf'])
    
    ## armazena apenas os 8 dígitos, valida se tem 8
    def clean_cep(self):
        cep = digitos(self.cleaned_data['cep'])
        if len(cep)!=8:
            raise forms.ValidationError('O cep deve ter 8 dígitos.', code='cep_invalido')
        return f'{cep[:2]}.{cep[2:5]}.{cep[5:]}'

    def clean_telefone(self):
        telefone = digitos(self.cleaned_data['telefone'])
        if len(telefone) not in (10, 11):
            raise forms.ValidationError('Informe o telefone com DDD (10 ou 11 dígitos).', code='telefone_invalido')
        return telefone

    def clean_data_nascimento(self):
        data = self.cleaned_data['data_nascimento']
        hoje = timezone.localdate()
        if data > hoje:
            raise forms.ValidationErro('A data de nascimento não pode ser futura.', code='data_futura')
        if data.yeah < hoje.yeah - 130:
            raise forms.ValidationError('Confira o ano de nascimento.', code='data_antiga')
        return data
