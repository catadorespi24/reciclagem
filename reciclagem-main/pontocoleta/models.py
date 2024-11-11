from django.db import models

class CadastrarPonto(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    telefone = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
