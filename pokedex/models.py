from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4,max_digits=6)
    height = models.DecimalField(decimal_places=4,max_digits=6)
    
    def __str__(self):
        return self.name
    
class Coach(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField(null=False)
    date_of_birth = models.DateField(null=False)
    def __str__(self):
        return f"{self.name} {self.last_name}"