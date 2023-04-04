from Pokemon import Pokemon
from Pokedex import Pokedex
import os

RED = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


pokedex = Pokedex()

geodude = Pokemon('geodude', 'rock', 'ground', 0.4, 20)
pikachu = Pokemon('pikachu', 'electric', 'electric', 0.4, 6)
blastoise = Pokemon('blastoise', 'water', 'water', 1.6, 85.5)

pokedex.lista_pokemon.append(geodude)
pokedex.lista_pokemon.append(pikachu)
pokedex.lista_pokemon.append(blastoise)

message = ''

while message != 'Acertou':
    pokemon_name = input("Digite o nome do pokemon: ")
    
    pokemon = pokedex.get_pokemon(pokemon_name)
    print(pokemon.name)
    message = pokedex.compare_pokemon(pokemon, geodude)
    if message != 'Acertou':
        print(message+os.linesep)

print(GREEN+'Acertou'+RESET)     