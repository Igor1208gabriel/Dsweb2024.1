from django.shortcuts import render, get_object_or_404
from django.http      import HttpResponseRedirect
from django.urls      import reverse
from .models import Question, Choice


def index(request): #parametro: HttpRequest
    enquetes = Question.objects.order_by('id')[:10]
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'inketes/index.html', contexto)


def detalhes(request, pergunta_id):
    que      = get_object_or_404(Question, pk = pergunta_id)
    contexto = {"inkete": que}
    return render(request, 'inketes/detalhes.html', contexto)


def votacao(request, pergunta_id):
    que = get_object_or_404(Question, pk=pergunta_id)
    try:
        idalt = request.POST['choice']
        alt   = que.choice_set.get(pk=idalt)
    except (KeyError, Choice.DoesNotExist):
        contexto = {
            'inkete': que,
            'error': 'Você precisa selecionar uma alternativa'
            }
        return render(request, 'inketes/detalhes.html', contexto)
    else:
        alt.votes += 1
        alt.save()
        return HttpResponseRedirect(reverse(
            'inketes:resultado', args=(pergunta_id,)
            ))



def resultado(request, pergunta_id):
    que = get_object_or_404(Question, pk = pergunta_id)
    return render(request, 'inketes/resultado.html', {"inkete": que} )


















