from django.db import models

class CadastroUsuario(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50)
    telefone = models.IntegerField()
    senha = models.CharField(max_length=100)
    confirme_senha = models.CharField(max_length=100)

    def __str__ (self) -> str:
        return self.nome

class Login(models.Model):
    apelido = models.CharField(max_length=50)
    senha = models.CharField(max_length=100)

    def __str__ (self) -> str:
        return self.apelido