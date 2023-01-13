from django.db import models

# Create your models here.
class Foodtable(models.Model):
    fname=models.CharField(max_length=10)

    def __str__(self):
        return self.fname

class Exercisetable(models.Model):
    ename=models.CharField(max_length=10)

    def __str__(self):
        return self.ename






