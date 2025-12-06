from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='trainers/', null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPE = {
        ('A','Agua'),
        ('F','Fuego'),
        ('T','Tierra'),
        ('P','Planta'),
        ('E','Eléctrico'),
        ('L','Lagartija'),
    }
    tipo = models.CharField(max_length=30,choices=POKEMON_TYPE, null=False)
    weight = models.DecimalField(decimal_places=4,max_digits=6)
    height = models.DecimalField(decimal_places=4,max_digits=6)
    picture = models.ImageField(upload_to='pokemons/',null=True,blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
