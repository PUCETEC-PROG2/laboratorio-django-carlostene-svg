from django.contrib import admin
from .models import Pokemon, Coach

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass 

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    pass 