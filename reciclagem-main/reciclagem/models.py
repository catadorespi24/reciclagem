from django.db import models

LISTA_CATEGORIAS = (
    ("GRANDES_EQUIPAMENTOS","Grandes Equipamentos"),
    ("PEQUENOS_EQUIPAMENTOS/ELETROPORTATEIS", "Pequenos Equipamentos ou Eletroportáteis"),
    ("EQUIPAMENTOS_INFORMATICA/TELEFONIA", "Equipamentos de Informática ou Telefonia"),
    ("PILHAS/BATERIAS", "Pilhas ou Baterias portáteis"),
)

# Criar o Residuo Eletronico
class AdicionarProduto(models.Model):
    produto = models.CharField(max_length=100)
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=50, choices=LISTA_CATEGORIAS)

    def __str__(self):
        return self.produto

# Create your models here.
