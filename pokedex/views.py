from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.
def home(request, pokemon_id):
    # CORREÇÃO 2: Coloquei o 'f' antes da string para o Python substituir o valor
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    
    response = requests.get(url)
    
    # Dica: Se o ID não existir (ex: 9999), vai dar erro aqui. 
    # O ideal seria verificar if response.status_code == 200, mas vamos manter simples.
    poke_dado = response.json()

    # Como é um pokemon só, não usamos o primeiro 'for' que você tinha.
    # Vamos direto para o tratamento dos tipos.
    tipos = []
    for t in poke_dado['types']:
        tipos.append(t['type']['name'])

    # Montamos o dicionário único
    pokemon_unico = {
        'name': poke_dado['name'],
        'image': poke_dado['sprites']['front_default'],
        'height': poke_dado['height'],
        'weight': poke_dado['weight'],
        'types': tipos,
        'id': poke_dado['id'],
    }
    
    # CORREÇÃO 3: O seu HTML espera uma lista (por causa do {% for %}).
    # Então colocamos esse único dicionário dentro de uma lista.
    pokemons = [pokemon_unico]

    return render(request, 'pokedex/home.html', {'pokemons': pokemons})


# name
# ability / name
# height
# id
# move / name

    # return render(request, 'pokedex/home.html', {'pokemons': pokemons})

    