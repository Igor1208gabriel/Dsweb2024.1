from django.shortcuts import render
from django.http import HttpResponse

def index(request): #parametro: HttpRequest
    return HttpResponse("<h1>Bom <u>dia!</u></h1>") #Retorno: HttpResponse