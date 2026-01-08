from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Aluno


# Create your views here.
def teste(request):
    return render(request, 'alunos/index.html')

def criar_aluno(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        return render (request, 'alunos/criar_alunos.html', {'alunos': alunos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nota = request.POST.get('nota')

        aluno = Aluno(
            nome = nome ,
            email = email ,
            nota = nota,
        )
        aluno.save()

        return redirect('alunos:criar_aluno')
    
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()

    return redirect('alunos:criar_aluno')

def atualizar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    aluno.nome = nome
    aluno.email = email
    aluno.save()

    return redirect('alunos:criar_aluno')