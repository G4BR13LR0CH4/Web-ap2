from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
# Create your models here.
