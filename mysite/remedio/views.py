from django.shortcuts import render, redirect
from .models import Remedio
from django.views import View


class RemedioView(View):

    def get(self, request, *args, **kwargs):
        remedio, _ = Remedio.objects.get_or_create(id=1)
        return render(request, "remedio/main.html", {"tomou": remedio.tomou})

    def post(self, request, *args, **kwargs):
        remedio, _ = Remedio.objects.get_or_create(id=1)
        remedio.tomou = True  # Só altera o estado para 'True' se o botão for pressionado.
        remedio.save()
        return redirect('remedio:remedio')  # Usar redirect para evitar duplicação de POST.
