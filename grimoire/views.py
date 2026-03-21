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
# Create your views here.
