from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request): #parametro: HttpRequest
    enquetes = Question.objects.order_by('pub_date')[:10]
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'inketes/index.html', contexto)


def detalhes(request, pergunta_id):
    que = get_object_or_404(Question, pk = pergunta_id)
    contexto = {"inkete": que}
    return render(request, 'inketes/detalhes.html', contexto)


def votacao(request, pergunta_id):
    resultado = "VOTAÇÃO da inkete de número %s"
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = 'RESULTADO da inkete de número %s'
    return HttpResponse(resultado % pergunta_id)



#mudança pra commitar