from django.urls import path
from . import views
import include

app_name = 'alunos'
urlpatterns = [
    path('teste/', views.teste, name="index"),
    path('criar_aluno/', views.criar_aluno, name='criar_aluno'),
]
