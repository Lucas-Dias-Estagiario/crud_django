from django.urls import path
from . import views
import include

app_name = 'alunos'
urlpatterns = [
    path('teste/', views.teste, name="index"),
    path('criar_aluno/', views.criar_aluno, name='criar_aluno'),
    path('deletar_aluno/<int:id>/', views.deletar_aluno, name="deletar_aluno"),
    path('atualizar_aluno/<int:id>/', views.atualizar_aluno, name="atualizar_aluno"),
]
