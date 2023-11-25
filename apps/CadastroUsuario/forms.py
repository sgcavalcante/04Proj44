from django import forms
from .models import CadastroPacientes,Image,ImageA
class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label = 'Usuário',
        required=True,
        max_length=50,
        widget= forms.TextInput(
            attrs = {
                'placeholder':'Usuário'
            }
        )
    )

    senha = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=12,
        widget= forms.PasswordInput(
            attrs={
            'placeholder':'Senha'
            }
        )
    )

class CadastroPacientesForm(forms.ModelForm):
    class Meta:
        model = CadastroPacientes
        fields = ['nome','telefone','email','data_nascimento','profissao','cep','estado','cidade','bairro','numero','complemento','alergia','doencas_conhecidas']   



class ImageForm(forms.ModelForm):
    class Meta: 
        model = Image
        fields = ("name","imagem")



class ImageAForm(forms.ModelForm):
    class Meta: 
        model = ImageA
        fields = ['name','imagem','nome']

