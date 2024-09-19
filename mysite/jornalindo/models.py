
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=30, blank=False, null=False)
    senha = models.CharField(max_length=20, blank=False, null=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.usuario}"

class Edicao(models.Model):
    edicaoid = models.AutoField(primary_key=True)
    data = models.DateField(default=timezone.now)
    nome = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return f"{self.nome}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=50, blank=False)
    texto = models.CharField(max_length=1024, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}\n {self.texto}\n {self.usuario}\n {self.edicao}"

class Comentario(models.Model):
    texto = models.CharField(max_length=1024, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.texto}\n {self.usuario}\n {self.noticia}\n {self.noticia.edicao}"
