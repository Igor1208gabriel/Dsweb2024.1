from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Edicao, Noticia, Comentario
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class CadastroForm(forms.ModelForm):
    nome_usuario = forms.CharField(max_length=100, required=True, label='Nome de Usuário')
    senha = forms.CharField(widget=forms.PasswordInput, required=True, label='Senha')

    class Meta:
        model = Usuario
        fields = ["nome_usuario", "senha"]

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['nome_usuario'],
            password=self.cleaned_data['senha']
        )
        usuario = super().save(commit=False)
        usuario.usuario = user

        if commit:
            usuario.save()
        return usuario


class CadastroNoticiaForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100, required=True, label='titulo')
    texto = forms.CharField(max_length=1024, required=True, label='texto')
    class Meta:
        model = Noticia
        fields = ['titulo', 'texto']


class CadastroComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 2}),
        }


class EdicaoForm(forms.ModelForm):
    nome = forms.CharField(max_length=100, required=True, label="nome")
    class Meta:
        model = Edicao
        fields = ["nome"]






