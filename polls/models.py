from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



    #no terminal:
    # python manage.py migratemport

    #configurar o módulo polls p ser reconhecido mo arquivo pasta-projeeto/settings.py incluir o módulocomo INSTALLED_APPS
    # python manage.py makemigrations

   # pip install -r requirements.txt