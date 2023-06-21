from django.db import models

import datetime

from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text






    






    #no terminal:
    # python manage.py migratemport

    #configurar o módulo polls p ser reconhecido mo arquivo pasta-projeeto/settings.py incluir o módulocomo INSTALLED_APPS
    # python manage.py makemigrations

   # pip install -r requirements.txt