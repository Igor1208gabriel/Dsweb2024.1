from django.shortcuts import render
from django.http import HttpResponse

def index(request): #parametro: HttpRequest
    return HttpResponse("""
    <h1>Desenvolvimento de Sistemas Web</h1>
    <h2>2024.1</h2>
    <h3>20231014040009</h3>
    <h4>Igor Gabriel dos Santos</h4>
    """
    ) #Retorno: HttpResponse