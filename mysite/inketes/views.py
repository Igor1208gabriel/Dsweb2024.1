from django.shortcuts   import render, get_object_or_404
from django.http        import HttpResponseRedirect
from django.urls        import reverse
#from django.views       import generic
from .models            import Question, Choice


'''
class IndexView():
    template_name = 'inketes/index.html'
    def get_queyset(self):
        return Question.objecs.order_by('id')

class DetalhesView(generic.DetailView):
    model = Question

class ResultadoView(generic.DetailView):
    model = Question
    template_name = 'inketes/resultado.html'

'''
def index(request): #parametro: HttpRequest
    enquetes = Question.objects.order_by('id')[:10]
    return render(request, 'inketes/index.html', {'lista_enquetes': enquetes} )


def detalhes(request, pergunta_id):
    que = get_object_or_404(Question, pk = pergunta_id)
    return render(request, 'inketes/detalhes.html', {"inkete": que} )


def resultado(request, pergunta_id):
    que = get_object_or_404(Question, pk = pergunta_id)
    return render(request, 'inketes/resultado.html', {"inkete": que} )





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




















