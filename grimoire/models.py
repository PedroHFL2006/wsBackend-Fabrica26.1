from django.db import models

class Casa(models.Model):
    nome = models.CharField(max_length=50)
    fundador = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
    casa = models.ForeignKey(Casa, on_delete=models.SET_NULL, null=True, related_name='membros')

    def __str__(self):
        return self.nome

# Create your models here.
