from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Aluno(models.Model):
    matricula = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=200)
    ace1 = models.PositiveSmallIntegerField("Projetos e programas", validators=[MaxValueValidator(200)])
    ace2 = models.PositiveSmallIntegerField("Cursos e eventos", validators=[MaxValueValidator(200)])
    ace3 = models.PositiveSmallIntegerField("Prestação de serviços", validators=[MaxValueValidator(200)])
    ace4 = models.PositiveSmallIntegerField("Disciplinas extensionista", validators=[MaxValueValidator(200)])
    
    def __str__(self):
        return self.matricula
    
    @property
    def horas(self):
        return self.ace1 + self.ace2 + self.ace3 + self.ace4

    
