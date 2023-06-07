from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls)
]
urlpatterns = [
   ...
   path('pergunta/<int:question_id>', views.exibe_questao, name='exibe_questao')
]
