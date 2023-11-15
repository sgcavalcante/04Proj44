from django import forms

class LoginForm(forms.Form):

    nome_login = forms.CharField(
        
        label = 'Nome de Login',
        required= True,
        max_length= 50,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Seu Login aqui...'
            }
        )    
    )

    senha = forms.CharField(
            label = 'Senha',
            required = True,
            max_length=20,
            widget = forms.PasswordInput(
                attrs = {
                    'placeholder':'Sua senha aqui...'
                }
                )
            )
 
    
    
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)