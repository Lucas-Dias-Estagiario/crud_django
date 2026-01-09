from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import requests

def home(request, pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    
    response = requests.get(url)
    poke_dado = response.json()

 
    tipos = []
    for t in poke_dado['types']:
        tipos.append(t['type']['name'])

    peso_kg = poke_dado['weight']
    peso_kg = peso_kg / 10

    altura_m = poke_dado['height']
    altura_m = altura_m / 10

    pokemon_unico = {
        'name': poke_dado['name'],
        'image': poke_dado['sprites']['front_default'],
        'height': altura_m,
        'weight': peso_kg,
        'types': tipos,
        'id': poke_dado['id'],
    }
    
    pokemons = [pokemon_unico]
    # return HttpResponse(poke_dado['types'])
    return render(request, 'pokedex/home.html', {'pokemons': pokemons})


# name
# ability / name
# height
# id
# move / name

    # return render(request, 'pokedex/home.html', {'pokemons': pokemons})

def proximo_pokemon(request, pokemon_id):
    pokemon_id = pokemon_id + 1

    return redirect('pokedex:index', pokemon_id=pokemon_id)

def anterior_pokemon(request, pokemon_id):
    pokemon_id = pokemon_id - 1

    return redirect('pokedex:index', pokemon_id=pokemon_id)

def ultimo_pokemon(request, pokemon_id):
    pokemon_id = 1025
    
    return redirect('pokedex:index', pokemon_id=pokemon_id)
