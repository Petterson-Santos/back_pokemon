from Pokemon import Pokemon
from Pokedex import Pokedex
import os

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
    message = pokedex.compare_pokemon(pokemon, geodude)

    print(pokemon.name+'\n'+message+os.linesep)

print('Acabou')