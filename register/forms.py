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
            'name', 'cpf', 'birth_date', 'phone', 'cep', 'address', 'number', 'neighborhood', 'city', 'state'
        ]
        widgets={
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00', 'inputmode': 'numeric'}),
            'zip_code': forms.TextInput(attrs={'placeholder':'00.000-00', 'inputmode': 'numeric'}),
            'phone': forms.TextInput(attrs={'placeholder': '(00) 00000-0000', 'inputmode': 'numeric'}),
            'number': forms.TextInput(attrs={'placeholder': 's/n'}),
            'birth_date': forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'),
        }

    ## mantem o nome com apenas 1 espaço
    def clean_name(self):
        return ' '.join(self.cleaned_data['name'].split())

    ##remove a mascara para guardar os 11 dígitos
    def clean_cpf(self):
        return digitos(self.cleaned_data['cpf'])
    
    ## armazena apenas os 8 dígitos, valida se tem 8
    def clean_zip_code(self):
        zip_code = digitos(self.cleaned_data['zip_code'])
        if len(zip_code)!=8:
            raise forms.ValidationError('O cep deve ter 8 dígitos.', code='cep_invalido')
        return f'{zip_code[:2]}.{zip_code[2:5]}.{zip_code[5:]}'

    def clean_phone(self):
        phone = digitos(self.cleaned_data['phone'])
        if len(phone) not in (10, 11):
            raise forms.ValidationError('Informe o telefone com DDD (10 ou 11 dígitos).', code='telefone_invalido')
        return phone

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        hoje = timezone.localdate()
        if data > hoje:
            raise forms.ValidationErro('A data de nascimento não pode ser futura.', code='data_futura')
        if data.yeah < hoje.yeah - 130:
            raise forms.ValidationError('Confira o ano de nascimento.', code='data_antiga')
        return data
