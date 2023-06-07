from django.shortcuts import render


from polls.models import Question, Choice

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, seja bem-vindo a enquete.")

def admin(request):
    return HttpResponse("admin.site.urls")

def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)
    
    if questao is not None:
        # questao.question_text
        return HttpResponse(questao.question_text)
    
    return HttpResponse('Não existe questão a exibir')
    
