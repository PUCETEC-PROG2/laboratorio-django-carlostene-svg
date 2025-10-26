from django.http import HttpResponse
from django.template import loader
from .models import Pokemon,Coach

def index(request):
    pokemons = Pokemon.objects.all()
    coachs=Coach.objects.all()
    template = loader.get_template('index.html')
    context = {
        'pokemons': pokemons,
        'coachs': coachs
    }
    return HttpResponse(template.render(context, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def coach(request, coach_id):
    coach = Coach.objects.get(id = coach_id)
    template = loader.get_template('display_coach.html')
    context = {
        'coach': coach
    }
    return HttpResponse(template.render(context, request))