from django.shortcuts import render, redirect, get_object_or_404
from .models import Edicao, Noticia, Comentario, Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CadastroForm, LoginForm, CadastroNoticiaForm, CadastroComentarioForm, EdicaoForm
from django.contrib.auth import authenticate, login
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        edicoes = Edicao.objects.all()[::-1]
        return render(request, 'jornalindo/index.html', {"edicoes": edicoes, "form": EdicaoForm()})

    def post(self, request, *args, **kwargs):
        form = EdicaoForm(request.POST)
        if form.is_valid():
            edicao = form.save(commit=False)
            edicao.save()
        else:
            form = EdicaoForm()
        edicoes = Edicao.objects.all()[::-1]
        return render(request, "jornalindo/index.html", {"edicoes": edicoes, "form": form})


def EdicaoDetail(request, id):
    edicao = get_object_or_404(Edicao, pk=id)
    noticias = Noticia.objects.filter(edicao=edicao)
    form = CadastroNoticiaForm()

    if request.method == "POST":
        form = CadastroNoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.edicao = edicao
            noticia.usuario = Usuario.objects.get(usuario=request.user)
            noticia.save()


    return render(request, "jornalindo/edicao.html", {"form": form, "edicao":edicao, "noticias": noticias[::-1]})

class CadastroNoticiaView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = CadastroNoticiaForm()
        return render(request, 'jornalindo/cadastro_noticia.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CadastroNoticiaForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('jornalindo:index')
        return render(request, 'jornalindo/cadastro_noticia.html', {'form': form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'jornalindo/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('jornalindo:index')
        return render(request, 'jornalindo/login.html', {'form': form})


class CadastroView(View):
    def get(self, request, *args, **kwargs):
        form = CadastroForm()
        return render(request, 'jornalindo/cadastro.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jornalindo:login')
        return render(request, 'jornalindo/cadastro.html', {'form': form})



def NoticiaDetail(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    comentarios = Comentario.objects.filter(noticia=noticia)

    if request.method == 'POST':
        form = CadastroComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.usuario = Usuario.objects.get(usuario=request.user)
            comentario.save()
            return redirect('jornalindo:noticia_slug', slug=noticia.slug)
    else:
        form = CadastroComentarioForm()

    context = {
        'noticia': noticia,
        'comentarios': comentarios,
        'form': form,
    }
    return render(request, 'jornalindo/noticia_slug.html', context)


def Pesquisa(request):
    query = request.GET.get('q')
    resultados = Noticia.objects.filter(texto__icontains=query)
    return render(request, 'jornalindo/pesquisa.html', {'resultados': resultados, 'query': query})


