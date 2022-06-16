from telnetlib import STATUS
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    capa = models.ImageField(upload_to='livros/capas/', blank=True)
    def __str__(self):
        return self.titulo