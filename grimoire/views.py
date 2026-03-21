from django.shortcuts import render, redirect
from .models import Pessoa

def wizards(request):
    if request.method == "POST":
        Pessoa.objects.create(
            nome=request.POST.get('nome'),
            idade=request.POST.get('idade'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone')
        )
        return redirect('wizards')
    
    pessoas = Pessoa.objects.all().values()

    contexto = {
        'meus_wizards': pessoas, 
    }

    return render(request, 'form.html', contexto)

def cadastrar_pessoa(request):
    return render(request, 'cadastrar_pessoa.html')

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method == "POST":
        pessoa.nome = request.POST.get('nome')
        pessoa.idade = request.POST.get('idade')
        pessoa.email = request.POST.get('email')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.save()
        return redirect('wizards')
    
    return render(request, 'editar_pessoa.html', {'pessoa': pessoa})

def deletar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('wizards')




# Create your views here.
