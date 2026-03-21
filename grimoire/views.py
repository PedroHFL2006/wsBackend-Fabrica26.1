from django.shortcuts import render
from .models import Pessoa

def wizards(request):
    pessoas = Pessoa.objects.all().values()
   
    contexto = {
        'meus_wizards': pessoas, 
    }

    return render(request, 'form.html', contexto)

# Create your views here.
