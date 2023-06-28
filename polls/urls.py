from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views
from django.http import HttpResponse
from .models import Question

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    # ex: /polls/
    path("", views.index, name="perguntas"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
]


# Leave the rest of the views (detail, results, vote) unchanged