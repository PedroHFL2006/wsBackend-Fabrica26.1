import requests
from django.shortcuts import render, redirect
from .models import Pessoa, Casa


def wizards(request):
    if request.method == "POST":
        casa_id = request.POST.get('casa')
        casa_selecionada = Casa.objects.get(id=casa_id)

        Pessoa.objects.create(
            nome=request.POST.get('nome'),
            idade=request.POST.get('idade'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            casa=casa_selecionada
        )
        return redirect('wizards')
    
    pessoas = Pessoa.objects.all()
    todas_as_casas = Casa.objects.all()

    contexto = {
        'meus_wizards': Pessoa.objects.all(),
        'casas': Casa.objects.all()
    }

    return render(request, 'form.html', contexto)

def cadastrar_pessoa(request):
    todas_as_casas = Casa.objects.all()
    return render(request, 'cadastrar_pessoa.html', {'casas': todas_as_casas})

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

def lista_hp(request):
    url = "https://hp-api.onrender.com/api/characters"

    try:
        response = requests.get(url, timeout=5)
        personagens = response.json()
        contexto = {
        'personagens': personagens[:10],
        'erro_api': False
        }
    except Exception as e:
        contexto = {
            'personagem': [],
            'erro_api': True
        }
        print(f"Erro ao acessar API: {e}")

    return render(request, 'lista_hp.html', contexto)

# Create your views here.
