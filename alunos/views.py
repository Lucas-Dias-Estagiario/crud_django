from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect


# Create your views here.
def teste(request):
    return render(request, 'alunos/index.html')

def criar_aluno(request):
    if request.method == 'GET':
        return render (request, 'alunos/criar_alunos.html')
    elif request.method == 'POST':
        print('oi')
