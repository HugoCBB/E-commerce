from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        label="Email",
        required=True,
        widget= forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite seu email"
            }
        )
    )

    senha = forms.CharField(
        max_length=70,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite a sua senha"
            }
        )
    )

class CadastroForm(forms.Form):
    nome = nome = forms.CharField(
        max_length=100,
        label="Nome",
        required=True,
        widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite o seu nome completo"
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        label="Email",
        required=True,
        widget= forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite seu melhor email"
            }
        )
    )
    
    senha1 = forms.CharField(
        max_length=70,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite a sua senha"
            }
        )
    )

    senha2 = forms.CharField(
        max_length=70,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite a senha novamente"
            }
        )
    )