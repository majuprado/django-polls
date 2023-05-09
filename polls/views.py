from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, seja bem-vindo a enquete.")

def sobre(request):
    return HttpResponse("Esse é um app de enquete.")